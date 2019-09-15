import numpy as np
import pandas as pd
import json
import tweepy as tw

CONSUMER_KEY="FnUkoVD3DqObS2DXYnj4v7dLI"
CONSUMER_SECRET_KEY="mB6VJXOhzNkAgdhbgaScujPPzN2UTnpl0P7Lr3et1K7xgMx2Pm"
ACCESS_KEY="1152979320459030528-eZoIOHdg1L0DbYRiXb6QFIpXGj5tDU"
ACCESS_KEY_SECRET="jzkk6RBQxx19B0k0tJ8M2UKAa5zq7OZjLmVj7BSOGJACC"

auth=tw.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_KEY,ACCESS_KEY_SECRET)

api=tw.API(auth)
search_words=input("Enter the serch word\n")
search_words=search_words+" -filter:retweets"
date_since = "2019-09-15"
tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items(100)
users_locs = [tweet.text for tweet in tweets]
tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['usertext'])
export_csv = tweet_text.to_csv (r'/home/ashish/Sentimeter/tee.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
print(tweet_text.head())
