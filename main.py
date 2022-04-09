import requests
from bs4 import BeautifulSoup
import smtplib
import os

#Email login
BOT_EMAIL = os.environ["USER"]
PWD = os.environ["PWD"]
SMTP_SERVER = "smtp.gmail.com"
NOTIFICATION_ADRESS = "your_email@gmail.com"

# Product setup by user
PRODUCT = "far cry 6 ps5" #Please write without polish letters
TARGET_PRICE = 100
CITY = "Wroclaw" #Please write without polish letters

# Send notification function
def send_notification(price, link):
    email = smtplib.SMTP(SMTP_SERVER)
    email.starttls()
    email.login(user=BOT_EMAIL, password=PWD)
    email.sendmail(from_addr=BOT_EMAIL,
                   to_addrs=NOTIFICATION_ADRESS,
                   msg=f"subject: Dobra cena na {PRODUCT}\n\n"
                       f"Okazja {price}PLN za {PRODUCT} \nLink do oferty: {link}")
    email.close()

# Converting variables
product = PRODUCT.replace(" ", "-").lower()
city = CITY.replace(" ", "-").lower()

# Get connection with URL
url = f"https://www.olx.pl/{city}/q-{product}/?search%5Border%5D=filter_float_price%3Aasc"
connection = requests.get(url)
connection.raise_for_status()

# Take content of website and setup variables for email notification (price_int and link for best offer)
content = BeautifulSoup(connection.text, "html.parser")
price_olx = content.find(name="p", class_="price").getText()
price_int = int(price_olx.replace(" zł", ""))
link = content.select_one(selector="td div h3 a")["href"]

#Rule for notification sending
if price_int < TARGET_PRICE:
    send_notification(price_int, link)
