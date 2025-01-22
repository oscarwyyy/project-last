import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Function to get movie details along with reviews
def get_movie_details(movie_url):
    response = requests.get(movie_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Safely extract movie title
    title_tag = soup.find('h1', class_='heading')
    title = title_tag.text.strip() if title_tag else 'No title available'
    
    # Safely extract rating
    rating_tag = soup.find('span', class_='rating')
    rating = rating_tag.text.strip() if rating_tag else 'No rating available'
    
    # Safely extract year
    year_tag = soup.find('span', class_='year')
    year = year_tag.text.strip() if year_tag else 'No year available'
    
    # Extract reviews (if any)
    reviews = []
    review_elements = soup.find_all('div', class_='entry')  # Adjust class name if necessary
    for review in review_elements:
        review_text = review.find('p').text.strip() if review.find('p') else 'No review text available'
        reviews.append(review_text)
    
    # Return the movie details as a dictionary
    return {'Title': title, 'Rating': rating, 'Year': year, 'Reviews': reviews}

# Scrape data for multiple movies (pages of Letterboxd)
def scrape_letterboxd_reviews(base_url, pages_to_scrape=10):
    all_movies = []
    
    for page_num in range(1, pages_to_scrape + 1):
        # Create the URL for each page
        page_url = f'{base_url}?page={page_num}'
        print(f"Scraping page {page_num}...")
        
        # Send GET request to fetch the page content
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all movie URLs on the page (adjust this if necessary)
        movie_links = soup.find_all('a', class_='film-link')  # The class name may vary
        
        for movie_link in movie_links:
            movie_url = movie_link['href']
            movie_url = f"https://letterboxd.com{movie_url}"
            
            # Scrape movie details
            movie_data = get_movie_details(movie_url)
            all_movies.append(movie_data)
            
            # Break if we have enough data
            if len(all_movies) >= 1000:
                break
        
        # Pause between requests to avoid overwhelming the server
        time.sleep(2)
        
        # Break if we reached 1000 records
        if len(all_movies) >= 1000:
            break

    return all_movies

# Set the base URL for Letterboxd film listings
base_url = 'https://letterboxd.com/films/popular/'

# Scrape movie reviews
movies_data = scrape_letterboxd_reviews(base_url, pages_to_scrape=50)  # Scrape 50 pages (adjust as needed)

# Create a DataFrame from the scraped data
df = pd.DataFrame(movies_data)

# Export the data to a CSV file
df.to_csv('letterboxd_movies_reviews.csv', index=False)

# Show the first few rows of the DataFrame
print(df.head())

