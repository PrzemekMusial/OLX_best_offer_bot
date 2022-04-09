# OLX_best_offer_bot in Python
Simple bot that sending notification email with price and link to offer from local market that could be interesting for you.

1. Setup BOT_EMAIL:

SMTP_SERRVER = smtp for BOT_EMAIL

BOT_EMAIL = bot adress which is sending email

PWD = password to BOT_EMAIL

NOTIFICATION_ADRESS = Your eamil adrees where you receive notification

2. Setup product:

All string parameters should be written without polish letters and between ""

PRODUCT = name of product that you want to search for

TARGET_PRICE = below this value notification will be send for lowest product price

CITY = city name

3. After setup you can put this bot in to the server and it will send you email notifications for local product offer for the lower price than TARGET_PRICE
