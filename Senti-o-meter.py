from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

import credentials
class TwitterStreamer():
    def stream_tweets(self,fetched_file_names):
        auth=OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET_KEY)
        auth.set_access_token(credentials.ACCESS_KEY,credentials.ACCESS_KEY_SECRET)
        listener=Streamy(fetched_file_names)
        stream=Stream(auth,listener)
        stream.filter(track=['#84rhg'])
    
    
class Streamy(StreamListener):
    def __init__(self,fetched_file_names):
        self.fetched_file_names=fetched_file_names
        
    def on_data(self,data):
        try:
            parsed_json = (json.loads(data))
            j=json.dumps(parsed_json)
            print(j)
            with open(self.fetched_file_names,'a') as tf:
                tf.write(j)
        except BaseException as e:
            print("Error on data %s" %str(e))
        return True
    
    def on_error(self,error):
        print(error)
        
fetched_file_names="tweets.json"
twitter_streamer=TwitterStreamer()
twitter_streamer.stream_tweets(fetched_file_names)        
        



