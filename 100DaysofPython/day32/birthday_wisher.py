from datetime import datetime
import pandas
import random
import smtplib # make connection

MY_EMAIL = "fazilaroushanbeg@gmail.com"
PASSWORD = "apzvrhsadcimbzjl"

today = datetime.now()
today_tuple =  (today.month, today.day)

# read form csv
data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letters/letter{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg="Subject: Happy Birthday!\n\n{contents}"
                            )