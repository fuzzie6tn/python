# maqsad beautiful souop ka ye hai k it extracts or pulls out the html tags from html file using python code
from bs4 import BeautifulSoup
# import lxml
with open("website.html") as htmlFile:
    content = htmlFile.read()

soup = BeautifulSoup(content,  'html.parser') # object created here and this one line of code completes the parsing
# print(soup.title)
# print(soup.prettify())
all_anchor_tags= soup.find_all(name="a")

# only text will be printed getText()
# href links will be printed using get()
for tag in all_anchor_tags:
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
company_url = soup.select_one(selector="#name")
print(company_url)