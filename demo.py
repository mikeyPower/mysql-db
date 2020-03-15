import re
import smtplib
import os
import requests
import urllib.request
from bs4 import BeautifulSoup
import MySQLdb
import datetime


DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ['DB_HOST']
DB_USERNAME = os.environ['DB_USERNAME']
DB_NAME = os.environ['DB_NAME']

def index():
    quotes = quote()
    cursor = connection()
    cur = cursor[0]
    db = cursor[1]
    todays_date = datetime.datetime.now()
    today = todays_date.strftime('%Y-%m-%d')
    try:
        cur.execute("INSERT INTO quotes(quote,quote_date,author) VALUES (%s, %s, %s)", (quotes[0], today, quotes[1]))
        db.commit()
    except:
        print()
    return 


#web scrapper to get quotes everyday
def quote():
# Set the URL you want to webscrape from
    url = 'https://www.brainyquote.com/quote_of_the_day'

# Connect to the URL
    response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

#print(soup)

#quote is in meta tag
    quote = soup.findAll('meta')
    quote_of_the_day = ""


#find the twtter description as the quote lies in that reference
    for i in quote:
        try:
            if(i.attrs['name']=='twitter:description'):
            #print(i.attrs['content'])
                quote_of_the_day = i.attrs['content']
        except:
            a = "Not everything that is faced can be changed, but nothing can be changed until it is faced.-James Baldwin"


        #check if quote of the day string is empty
    if not quote_of_the_day:
        quote_of_the_day = a

#remove quotes
    newstr = quote_of_the_day.replace('"', "")

#split string into quote and author
    spit = newstr.rsplit('-',1)
    return spit


# Start MySQL database connection returning connection state and database
def connection():
    dbconn = MySQLdb.connect(host = DB_HOST,
                             user = DB_USERNAME,
                             passwd = DB_PASSWORD,
                             db = DB_NAME)
    cur = dbconn.cursor()
    return (cur, dbconn)


if __name__ == '__main__':
    index()
