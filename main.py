import yagmail
import pandas
from news import NewsFeed
import datetime
import time


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['Interest'],
                         from_date=yesterday,
                         to_date=today)
    email = yagmail.SMTP(user="stefanpythonmail@gmail.com", password="Parola123!")
    email.send(to=row['Email'],
               subject=f"Your daily dose of {row['Interest']} is here!",
               contents=f"Hi {row['Name']},\nHere are your {row['Interest']} news from last week:\n\n{news_feed.get()}\n\nHave a nice day!\nStefan")


while True:
    if datetime.datetime.now().hour == 8 and datetime.datetime.now().minute == 30:
        df = pandas.read_excel('emaildb.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)