# import smtplib
#
# my_email = "fazilaroushanbeg@gmail.com"
# password = "trlpvnxratypoxap"
# #   trlp vnxr atyp oxap
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() # tls - transport layer security (makes it secure) way of securing our connection to our email server
#     # in simple words it encrypts the message and makes it impossible to read what's in our content of email
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="optimist.alishan@gmail.com",
#                         msg="Subject:Sending with subject\n\n i am fish, i am sending this message with python code")

# now = dt.datetime.now()
# year = now.year
# week_day = now.weekday()
# print(week_day)


import smtplib
import datetime as dt
import random

my_email = "fazilaroushanbeg@gmail.com"
password = "trlpvnxratypoxap"

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 2:
    with open("quotes.txt", "r") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject: Quote of the day\n\nSending you a random quote from my list of quotes\n{quote}")


