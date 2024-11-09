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
    for item in soup.find_all('div'):
        headline_tag = item.find('h2')  # Headlines are usually in <h3> tags
        if headline_tag:
            headline = headline_tag.get_text(strip=True)
        else:
            continue

        # Find the summary text (usually in <p> tags)
        summary_tag = item.find('p')
        summary = summary_tag.get_text(strip=True) if summary_tag else 'No summary available'

        # Find the link to the article
        link_tag = item.find('a', href=True)  # Extract the link to the full article
        if link_tag:
            link = 'https://www.bbc.com' + link_tag['href']
        else:
            link = 'No link available'

        # Get the date (use current date as a placeholder since BBC doesn't provide explicit article dates in the homepage)
        date = datetime.now().strftime("%Y-%m-%d")

        # Add the article to the list
        articles.append({
            'Title': headline,
            'Summary': summary,
            'Link': link,
            'Date': date
        })

    return articles

# Streamlit UI
def main():
    st.title('BBC News Scraper')

    # Fetch the latest articles
    articles = fetch_bbc_news()
    st.write("Select Data and Category to find Articles")

    # if not articles:
    #     st.write("No articles found!")
    #     return

    # Convert the list of articles to a Pandas DataFrame for easy filtering
    df = pd.DataFrame(articles)

    # Show the data in a table
    st.write("### Latest News Articles")
    # st.write(df)

    # Add a date filter widget
    filter_date = st.sidebar.date_input('Filter by Date (optional)', None)

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

    # Add a category filter widget (you can implement this depending on how you define categories)
    categories = ['World', 'Business', 'Politics', 'Technology', 'Science']  # These are just example categories
    selected_category = st.sidebar.selectbox("Select Category (optional)", categories)

    # Filter articles by selected category (if any)
    if selected_category != 'All':
        # In this case, we're not scraping categories directly from the homepage, 
        # so for this demo we will filter based on whether the summary contains the category keyword.
        filtered_category_df = df[df['Summary'].str.contains(selected_category, case=False, na=False)]
        if filtered_category_df.empty:
            st.write(f"No articles found for the category '{selected_category}'.")
        else:
            st.write(f"Articles related to {selected_category}:")
            st.write(filtered_category_df)
    else:
        st.write(df)

    # Display individual article details with clickable links
    st.write("### Article Details")
    for article in articles:
        st.write(f"**[{article['Title']}]({article['Link']})**")
        st.write(f"Summary: {article['Summary']}")
        st.write(f"Published on: {article['Date']}")
        st.markdown('---')

# Run the main function
if __name__ == "__main__":
    main()
