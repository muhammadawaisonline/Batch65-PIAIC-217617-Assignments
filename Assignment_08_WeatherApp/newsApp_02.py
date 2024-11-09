import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import streamlit as st

# Function to fetch the latest BBC news articles
def fetch_bbc_news():
    url = 'https://www.bbc.com/news'  # BBC News homepage URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        # Send GET request to BBC News
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching the website: {e}")
        return []

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # List to store articles
    articles = []

    # Look for article blocks by the correct tag and class names
    for item in soup.find_all('div', class_='gs-c-promo'):
        title_tag = item.find('h2')  # Assuming the headline is inside an <h3> tag
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            continue

        link_tag = item.find('a', href=True)  # Look for the <a> tag to get the article's link
        if link_tag:
            link = 'https://www.bbc.com' + link_tag['href']
        else:
            continue

        # Look for summary in the <p> tag or similar
        summary_tag = item.find('p')
        summary = summary_tag.get_text(strip=True) if summary_tag else 'No summary available'

        # Use current date for simplicity
        date = datetime.now().strftime("%Y-%m-%d")

        # Add article details to the list
        articles.append({
            'Title': title,
            'URL': link,
            'Summary': summary,
            'Date': date
        })

    return articles

# Streamlit UI
def main():
    st.title('BBC News Scraper')

    # Fetch the latest articles
    articles = fetch_bbc_news()

    if not articles:
        st.write("No articles found!")
        return

    # Convert articles to a Pandas DataFrame for easy filtering
    df = pd.DataFrame(articles)

    # Show the data in a user-friendly table
    st.write("### Latest News Articles")
    st.write(df)

    # Add a date filter widget
    filter_date = st.date_input('Filter by Date (optional)', None)

    if filter_date:
        # Convert the 'Date' column to datetime to compare with the selected date
        df['Date'] = pd.to_datetime(df['Date'])
        filtered_df = df[df['Date'].dt.date == filter_date]

        if filtered_df.empty:
            st.write("No articles found for this date.")
        else:
            st.write(filtered_df)
    else:
        st.write(df)

    # Display individual article details
    st.write("### Article Details")
    for article in articles:
        st.write(f"**[{article['Title']}]({article['URL']})**")
        st.write(f"Summary: {article['Summary']}")
        st.write(f"Published on: {article['Date']}")
        st.markdown('---')

if __name__ == "__main__":
    main()
