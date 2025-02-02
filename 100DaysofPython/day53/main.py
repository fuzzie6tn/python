from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%2", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_links_elements = soup.select(".list-card-top")

links=[]
link in all_links_elements:
href= link["href"]
print(href)

if "http" not in href:
    all_links.append(f"http://www.zillow.com {href}")

else:
    all_links_elements