import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
from datetime import datetime

# Function to fetch BBC News articles
def fetch_bbc_news():
    url = 'https://www.bbc.com/news'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
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

    # Look for article blocks by the correct class
    # BBC News uses a "gs-c-promo" class for promo content
    for item in soup.find_all('div', class_='gs-c-promo'):
        title_tag = item.find('h3')
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            continue

        link_tag = item.find('a', href=True)
        if link_tag:
            link = 'https://www.bbc.com' + link_tag['href']
        else:
            continue

        # Optional: Some articles might have summaries in the aria-label attribute
        summary_tag = item.find('p')
        summary = summary_tag.get_text(strip=True) if summary_tag else 'No summary available'

        # Use current date for simplicity in this example
        date = datetime.now().strftime("%Y-%m-%d")

        # Add to articles list
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

    # Display the raw dataframe in the Streamlit app
    st.write("### Latest News Articles")
    st.write(df)

    # Optional: Allow the user to filter by date (this is now optional)
    filter_date = st.date_input('Filter by Date (optional)', None)

    # If a date is selected, filter articles by the selected date
    if filter_date:
        df['Date'] = pd.to_datetime(df['Date'])
        filtered_df = df[df['Date'].dt.date == filter_date]

        if filtered_df.empty:
            st.write("No articles found for this date.")
        else:
            st.write(filtered_df)
    else:
        # If no date filter is selected, show all articles
        st.write(df)

    # Display individual article links and summaries
    st.write("### Article Details")
    for article in articles:
        st.write(f"**[{article['Title']}]({article['URL']})**")
        st.write(f"Summary: {article['Summary']}")
        st.write(f"Published on: {article['Date']}")
        st.markdown('---')

if __name__ == "__main__":
    main()
