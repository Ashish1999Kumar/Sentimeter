from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

import credentials
class Streamy(StreamListener):
    
    def on_data(self,data):
        parsed=json.loads(data)
        print(json.dumps(parsed, indent=2, sort_keys=True))
        return True
    
    def on_error(self,error):
        print(error)
        
        

auth=OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_KEY,credentials.ACCESS_KEY_SECRET)
listener=Streamy()
stream=Stream(auth,listener)

stream.filter(track=['#ashes'])
