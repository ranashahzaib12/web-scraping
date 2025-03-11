import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://83.217.23.34",
    "https": "http://45.140.143.77"
}

url = "https://www.amazon.com/s?k=samsung&crid=XQQJ2J26JHOZ&sprefix=samsung%2Caps%2C533&ref=nb_sb_noss_1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Setting verify=False to bypass SSL verification
r = requests.get(url, headers=headers, proxies=proxies)

soup = BeautifulSoup(r.text, "html.parser")

print(soup.prettify())
