import numpy as np
import pandas as pd
import json
import tweepy as tw
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

CONSUMER_KEY=""
CONSUMER_SECRET_KEY=""
ACCESS_KEY="1152979320459030528-1AJh1PKmKMO70xOhAjsrXz23UXvMog"
ACCESS_KEY_SECRET="yekeVb4fghMKJdLXJafMQWsIXnDTRRm5rtXSpvul8Yo6p"

auth=tw.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_KEY,ACCESS_KEY_SECRET)

api=tw.API(auth)
search_words=input("Enter the serch word\n")
search_words=search_words+" -filter:retweets"
date_since = "2019-09-15"
tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items(10)
users_locs = [tweet.text for tweet in tweets]
token_words=[]

for i in users_locs:
    token_words.append(word_tokenize(i))
    
stop_words=set(stopwords.words('english'))
filtered=[]

for i in token_words:
    x=[w for w in i if not w in stop_words]
    filtered.append(x)

print(filtered[1])
tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['usertext'])
export_csv = tweet_text.to_csv (r'/home/ashish/Sentimeter/tee.csv', index = None, header=True)
print(tweet_text.head())
