import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Qs"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, "lxml")

# print(soup.prettify())
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    # Construct the email message
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login("fazilaroushanbeg@gmail.com", "apzvrhsadcimbzjl")

        # Encode the message in UTF-8 to handle non-ASCII characters
        connection.sendmail(
            from_addr="fazilaroushanbeg@gmail.com",
            to_addrs="fazilaroushanbeg@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8")
        )
