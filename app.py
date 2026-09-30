import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')



st.set_page_config(page_title='Weather App',page_icon="🌥️")

st.title('Weather App⛅')

st.write('Enter The City Name and click on the page to fetch the weather data')

city = st.text_input('Enter the city name')

if st.button('Fetch weather Data'):
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(API_URL)

    if response.status_code == 200:
        st.success('weather data fetch successfully')
        data = response.json()

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        condition = data['weather'][0]['main']
        country = data['sys']['country']
        name = data['name']

        st.header(f"{name}, {country}")

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        col1.metric('Temperature', f"{temperature} °C 🌡")
        col2.metric('Humidity', f"{humidity}%💧")
        col3.metric('Wind Speed', f"{wind_speed} m/s🌬")
        col4.metric('Condition', condition,"☁")

    else:
        st.error("Invalid city name or API request failed")
