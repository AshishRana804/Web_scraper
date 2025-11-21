import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Set to keep track of URLs we have already visited
visited_urls = set()

# The base URL of the website we want to scrape
# We will only scrape pages that start with this URL
BASE_URL = "https://www.arlearningonline.com/"  # Replace with your website URL

def scrape_page(url):
    """
    Scrapes a single page, extracts its text, and finds all internal links.
    """
    if url in visited_urls:
        return  # Skip if we've already visited this page

    print(f"Scraping: {url}")
    visited_urls.add(url)

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Check for errors (like 404)
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # --- 1. Extract Text ---
    # Find all relevant text tags
    # You can add more tags here if needed (e.g., 'li', 'span')
    text_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'title'])
    
    page_text = ""
    for tag in text_tags:
        text = tag.get_text().strip()
        if text:
            page_text += text + "\n\n"
    
    # Save the extracted text to our main file
    if page_text:
        with open("scraped_content.txt", "a", encoding="utf-8") as f:
            f.write(f"--- CONTENT FROM: {url} ---\n")
            f.write(page_text)
            f.write("--------------------------------------\n\n")

    # --- 2. Find All Links and Scrape Them ---
    links = soup.find_all('a', href=True)
    
    for link in links:
        href = link['href']
        
        # Make the link absolute (e.g., /about -> https://www.site.com/about)
        full_url = urljoin(BASE_URL, href)
        
        # Parse the URL to remove anchors (#) or query params (?)
        parsed_url = urlparse(full_url)
        full_url = parsed_url._replace(query="", fragment="").geturl()

        # Check two conditions:
        # 1. Is it part of our base website?
        # 2. Have we visited it before?
        if full_url.startswith(BASE_URL) and full_url not in visited_urls:
            # Recursively call the function for the new link
            scrape_page(full_url)

# --- Main execution ---
if __name__ == "__main__":
    # Clear or create the output file
    open("scraped_content.txt", "w").close() 
    
    print(f"Starting scraper for: {BASE_URL}")
    
    # Start the process from the homepage
    scrape_page(BASE_URL)
    
    print("--- Scraping Finished ---")
    print(f"Total pages visited: {len(visited_urls)}")
    print("Content saved to 'scraped_content.txt'")