import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

# Setting verify=False to bypass SSL verification
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

