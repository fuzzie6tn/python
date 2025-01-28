from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for articles in articles:
    article_text = articles.getText()
    article_texts.append(article_text)
    article_link = articles.get("href")
    article_links.append(article_link)

article_upvote = [score.getText().split()[0] for score in soup.find_all("span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvote)

# highest upvotes ka text or link download karna hai
largest_number= max(article_upvote)
largest_index= article_upvote.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])