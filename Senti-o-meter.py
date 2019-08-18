import numpy as np
import pandas as pd
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from ast import literal_eval

import credentials

class twitter_authenticator():
    
    def authenticate_twitter_app(self):
        auth=OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET_KEY)
        auth.set_access_token(credentials.ACCESS_KEY,credentials.ACCESS_KEY_SECRET)
        return auth

class TwitterStreamer():
    
    def __init__(self):
        self.twitter_authenticate=twitter_authenticator()
    
    def stream_tweets(self,fetched_file_names):
        auth=self.twitter_authenticate.authenticate_twitter_app()
        listener=Streamy(fetched_file_names)
        stream=Stream(auth,listener)
        stream.filter(track=['#8299as'])
    
    
class Streamy(StreamListener):
    def __init__(self,fetched_file_names):
        self.fetched_file_names=fetched_file_names
        
    def on_data(self,datas):
        try:
            parsed_json = (json.loads(datas))
            print(parsed_json)
            text=parsed_json['text']
            with open(self.fetched_file_names,'a') as tf:
                tf.write('\n'+text) 
        except BaseException as e:
            print("Error on data %s" %str(e))
        return True
    
    def on_error(self,error):
        print(error)
        if error==420:
            return False
        
        
fetched_file_names="tweets.json"
twitter_streamer=TwitterStreamer()
twitter_streamer.stream_tweets(fetched_file_names)

        



