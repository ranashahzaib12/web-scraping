import requests
from bs4 import BeautifulSoup
import csv

def scrape_imdb():
    url = "https://www.imdb.com/chart/top/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        # Verify we're getting the correct page
        if "IMDb Top 250 Movies" not in response.text:
            raise ValueError("Captcha or redirect detected")

        soup = BeautifulSoup(response.text, 'html.parser')
        movies = []

        # Updated CSS selector for movie containers (July 2024)
        movie_list = soup.select('div.ipc-page-grid__item ul.ipc-metadata-list li.ipc-metadata-list-summary-item')

        if not movie_list:
            raise ValueError("No movie rows found. Check the HTML structure.")

        for movie in movie_list:
            # Extract title and remove ranking number
            title = movie.select_one('h3.ipc-title__text').get_text(strip=True).split('. ', 1)[-1]
            
            # Extract metadata (year, rating, etc.)
            metadata = movie.select('span.cli-title-metadata-item')
            year = metadata[0].get_text(strip=True) if len(metadata) > 0 else 'N/A'
            rating = movie.select_one('span.ipc-rating-star').get_text(strip=True).split()[0]

            movies.append([title, year, rating])

        return movies

    except Exception as e:
        print(f"Error during scraping: {str(e)}")
        return []

def save_to_csv(data, filename="imdb_top_movies.csv"):
    # THere could be an error that the Websites HTML structure could be changed so we have to resolve this issue
    if not data:
        print("No data to save. Skipping CSV writing.")
        return

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Year", "Rating"])
            writer.writerows(data)
        print(f"Successfully saved {len(data)} movies to {filename}")
    except Exception as e:
        print(f"Error saving CSV: {str(e)}")

if __name__ == "__main__":
    movies_data = scrape_imdb()
    save_to_csv(movies_data)