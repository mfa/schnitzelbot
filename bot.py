from credentials import API_KEY, API_SECRET, CLIENT_TOKEN, CLIENT_SECRET

import tweepy
import json
#from tweepy.streaming import StreamListener
#from tweepy import OAuthHandler
#from tweepy import Stream


class StdOutListener(tweepy.streaming.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        data = json.loads(data)
        print data.get('text')
        api.create_favorite(data.get('id'))
        api.create_friendship(data.get('user').get('id'))
        return True

    def on_error(self, status):
        print status

l = StdOutListener()
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(CLIENT_TOKEN, CLIENT_SECRET)
api = tweepy.API(auth)

stream = tweepy.Stream(auth, l)
stream.filter(track=['schnitzel'])
