import requests
import streamlit as st
st.title("JB Weather App ")
city =st.text_input("Enter City:")
button = st.button("Get Weather Info")
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b467cbdd7b3bfc7fea06dce564de4eb4&units=metric'.format(city)
if button:
    result = url
    res = requests.get(url)
    data = res.json()
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    st.write('Temperature:',temp,'°C')
    st.write('Wind:',wind)
    st.write('Pressure: ',pressure)
    st.write('Humidity: ',humidity)
    st.write('Description:',description)
else:
    st.write("Please enter city name")