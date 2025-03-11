import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

# Setting verify=False to bypass SSL verification
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

catalogue = soup.select("article",class_= "product_prod")

for book in catalogue:
    title = book.h3.a['title']
    price = book.find("p",class_="price_color")
    rating = book.find("p", class_ = "star-rating")["class"][1]
    availaibility = book.find("p", class_ = "instock availaibility")

    
print("Title:" , title)
print("Price", price)
print("rating:", rating)
print("Availaible:", availaibility)

# print(soup.prettify()) 