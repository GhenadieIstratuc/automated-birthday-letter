import smtplib
import datetime as dt
import pandas
from random import randint

now = dt.datetime.now()
actual_month = now.month
actual_day = now.day

my_email = "SENDER'S EMAIL"
my_password = "SENDER'S PASSWORD"

data = pandas.read_csv("birthdays.csv")
people_to_greet = data.to_dict(orient="records")
for person in people_to_greet:
    if person["month"] == actual_month and person["day"] == actual_day:
        with open(f"letter_templates/letter_{randint(1, 3)}.txt", "r") as letter:
            contents = letter.readline()
            contents = contents.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=person["email"],
                                msg=f"Subject:Happy Birthday!\n\n{contents}")
