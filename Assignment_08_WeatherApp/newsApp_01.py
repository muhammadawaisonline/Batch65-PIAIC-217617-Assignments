import requests
from bs4 import BeautifulSoup
import streamlit as st

url = " https://www.bbc.com/news"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")



st.title("BBC WEB Scraper")
headlines = soup.find_all("h2")

text =  soup.find_all("p")


for headline in headlines:
# print(headline.text) 
    st.write(headline.text)
    