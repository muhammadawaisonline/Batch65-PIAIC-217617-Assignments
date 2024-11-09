import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

# user_input = input("Enter Your City: ")
# city = user_input if user_input else "faisalabad"
# url = "https://google.com?q="+"weather"+city
# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# temp_1 = soup.find("span", class_ = "wob_t q8U8x")
# temp = soup.find("tag", id = "wob_tm")
# unit = soup.find("span", class_="wob_t")
# weather_condition = soup.find("span", id= "wob_dc")
# print(response.status_code)
# print(temp_1)
# print(unit)
# print(weather_condition)

st.title("Weather App")

user_input = st.text_input("Enter City Name to Check Weather Condition") 
city = user_input if user_input else "Faisalabad"

#from lxml import html
api_key = "bf91acb686e9392168c2cccf4f8027a4"
# city = "lahore"

# url = "https://weather.com/en-PK/weather/today/l/PKXX0006:1:PK?Goto=Redirected"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)

print(response.status_code)

# soup = BeautifulSoup(response.text, "lxml")

data= response.json()
city = data["name"]

temperature = data['main']['temp']

tem = round(temperature)

weather_condition = data['weather'][0]['description']

# st.text(city)
# st.text(tem)
# st.text(weather_condition) 
# print(city)
# print(tem, "℃")
# print(weather_condition)
# tags = soup.divs
# print(tags)
# print(data)



# Create a sample DataFrame
data = {
    "City": [city],
    "Temprature ℃": [tem],
    "Wheather Condition": [weather_condition]
}

df = pd.DataFrame(data)

# Display the DataFrame as a table
st.write(f"Here is the weather of {city}:")
st.write(df)


