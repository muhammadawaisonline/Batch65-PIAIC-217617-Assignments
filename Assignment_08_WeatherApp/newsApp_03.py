import requests
from bs4 import BeautifulSoup

# Function to fetch the headlines and text from BBC News
def fetch_bbc_headlines():
    url = 'https://www.bbc.com/news'  # BBC News homepage URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        # Send GET request to BBC News
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return []

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # List to store headlines and text
    articles = []

    # Find all the articles (using class names or tags specific to BBC)
    for item in soup.find_all("div"):
        headline_tag = item.find('h2')  # Headlines are usually in <h3> tags
        if headline_tag:
            headline = headline_tag.get_text(strip=True)

        # Find the text/summary
        summary_tag = item.find('p')  # Text is usually in <p> tags
        summary = summary_tag.get_text(strip=True) if summary_tag else 'No summary available'

        # Find the URL of the article
        link_tag = item.find('a', href=True)  # Extract the link to the full article
        if link_tag:
            link = 'https://www.bbc.com' + link_tag['href']
        else:
            link = 'No link available'

        # Add the headline, summary, and link to the articles list
        articles.append({
            'Headline': headline,
            'Summary': summary,
            'Link': link
        })

    return articles

# Main function to display the fetched data
def main():
    articles = fetch_bbc_headlines()

    if not articles:
        print("No articles found!")
        return

    # Print the headlines and summaries
    for idx, article in enumerate(articles, start=1):
        
        print(f"{idx}. {article['Headline']}")
        print(f"Summary: {article['Summary']}")
        print(f"Link: {article['Link']}")
        print('-' * 80)

# Run the main function
if __name__ == "__main__":
    main()
