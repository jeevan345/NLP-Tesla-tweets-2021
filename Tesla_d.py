from importlib.resources import path
import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import time

tweets = []
d0 = date(2013,10,11)
  
t=1
d1 = d0
d2 = d0 + datetime.timedelta(days=1)
m1 = 1

while True:    
    query = '"tesla" lang:en until:'
    _ = ' since:'
    query = query + str(d2)+_+str(d1)
    if d2>= date(2014,1,2): #d0 + relativedelta(months=12):
        print("done")
        break

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append([tweet.date, tweet.user.username, tweet.content])

    print(d1)
    # datee = datetime.datetime.strptime(str(d1), "%Y-%m-%d")
    # year = datee.year
    # month = datee.month
    # num = 1
    name = 'tesla='+str(d1)+'.json'
    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
    df.to_json(str(name), index = True)
    tweets=[]
    time.sleep(t+3)
    m1+= 1

    #  time.sleep(t+3)

    d1 = d1 + datetime.timedelta(days=1) 
    d2 = d2 + datetime.timedelta(days=1) 
    df.tail(1)
