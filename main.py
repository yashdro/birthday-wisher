
import datetime  as dt
import smtplib
import os
import pandas
import random


my_email = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month,today_day)
day_of_week = now.weekday()


print(today)


data = pandas.read_csv("birthdays.csv")



new_dict = {
    (row.month,row.day):row for (index,row) in data.iterrows()
}

print(new_dict)

if today in new_dict:
    birthday_person = new_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"] )

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password= MY_PASSWORD)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")




print(day_of_week)

with open("quotes.txt", "r", encoding="utf-8") as quote:
    contents = quote.readlines()

if day_of_week == 0:
    random_quote = random.choice(contents)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=MY_PASSWORD)
        connection.sendmail(from_addr=my_email, to_addrs="yashdrolia03@gmail.com", msg=f"Subject: Quote of the day\n\n{random_quote}".encode("utf-8"))
        print("Quote Sent")

else:
    print("today is not monday no quote sent")









