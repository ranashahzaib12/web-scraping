
import requests
from bs4 import BeautifulSoup
import csv


def scrape_books():
    url = "https://books.toscrape.com/catalogue/page-1.html"
    base_url = "https://books.toscrape.com/catalogue/"
    
    books_data = []  # List to store book details
    
    while url:  # Loop through all pages
        response = requests.get(url)  # Fetch the webpage
        soup = BeautifulSoup(response.text, "html.parser")  # Parse HTML
        
        # Find all book containers
        books = soup.find_all("article", class_="product_pod")
        
        for book in books:
            # Extract book title
            title = book.h3.a["title"]

            # Extract book price
            price = book.find("p", class_="price_color").text.strip()

            # Extract book rating (class names contain the rating)
            rating_class = book.find("p", class_="star-rating")["class"]
            rating = rating_class[1]  # Second class name is the rating (e.g., "Three")

            books_data.append([title, price, rating])  # Append data to the list

        # Check if there's a "Next" page button
        next_page = soup.find("li", class_="next")
        if next_page:
            url = "https://books.toscrape.com/catalogue/" + next_page.a["href"]
        else:
            url = None  # Stop loop if no next page

    return books_data

def save_to_csv(data, filename="books_data.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Rating"])  # Write header
        writer.writerows(data)  # Write book data

    print(f"Data saved to {filename}")



if __name__ == "__main__":
    books = scrape_books()
    save_to_csv(books)
