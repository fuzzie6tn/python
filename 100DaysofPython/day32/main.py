import smtplib

my_email = "fazilaroushanbeg@gmail.com"
password = "trlpvnxratypoxap"
#   trlp vnxr atyp oxap
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # tls - transport layer security (makes it secure) way of securing our connection to our email server
    # in simple words it encrypts the message and makes it impossible to read what's in our content of email
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="optimist.alishan@gmail.com",
                        msg="Subject:Sending with subject\n\n i am fish, i am sending this message with python code")