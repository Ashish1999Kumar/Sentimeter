import numpy as np
import pandas as pd
import re
import tweepy as tw
from datetime import date
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

CONSUMER_KEY=""
CONSUMER_SECRET_KEY=""
ACCESS_KEY="1152979320459030528-1AJh1PKmKMO70xOhAjsrXz23UXvMog"
ACCESS_KEY_SECRET="yekeVb4fghMKJdLXJafMQWsIXnDTRRm5rtXSpvul8Yo6p"

auth=tw.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_KEY,ACCESS_KEY_SECRET)

api=tw.API(auth)
search_words='#'+input("Enter the serch word\n")
search_words=search_words+" -filter:retweets"
date_since = date.today()
tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items(10)
users_locs = [tweet.text.lower() for tweet in tweets]

user_loc=[]
email='\shttp\S*'
for i in users_locs:
    punc_words=(re.sub('[^A-Za-z\s]+','',i))
    pattern=re.compile(email)
    user_loc.append(pattern.sub('',punc_words))
    
token_words=[]
for i in user_loc:
    token_words.append(word_tokenize(i))
    
stop_words=set(stopwords.words('english'))
filtered=[]

for i in token_words:
    x=[w for w in i if not w in stop_words]
    y=" ".join(x)
    filtered.append(y)

tweet_text = pd.DataFrame(data=filtered, 
                    columns=['usertext'])
export_csv = tweet_text.to_csv (r'/home/ashish/Sentimeter/tee.csv', index = None, header=True)
print(tweet_text.head())
