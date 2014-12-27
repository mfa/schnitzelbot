# -*- coding: utf-8 -*-

# set credentials in credentials.py
from credentials import API_KEY, API_SECRET, CLIENT_TOKEN, CLIENT_SECRET

import tweepy
import random
import json
from replies import replies_list


class StdOutListener(tweepy.streaming.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """

    last_own_tweet = None

    def on_data(self, data):
        data = json.loads(data)
        print(data.get('text'))
        try:
            # FIXME: how to test if already faved?
            api.create_favorite(data.get('id'))
        except:
            pass
        #if not data.get('user').get('id') in api.me().friends():
        #    api.create_friendship(data.get('user').get('id'))

        # reply to some of the tweets
        if random.randint(0, 10) == 4:
            # FIXME not the best way to to this:
            new_status = random.choice(replies_list)
            while new_status == self.last_own_tweet:
                new_status = random.choice(replies_list)
            last_own_tweet = new_status
            api.update_status(status='@%s %s' % (data.get('user').get('screen_name'),
                                                 last_own_tweet),
                              in_reply_to_status_id=data.get('id')
                          )

        return True

    def on_error(self, status):
        print(status)


l = StdOutListener()
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(CLIENT_TOKEN, CLIENT_SECRET)
api = tweepy.API(auth)

stream = tweepy.Stream(auth, l)
stream.filter(track=['schnitzel', '#schnitzel', '#schnitzelbot', '@schnitzelfollow', '#hackerschnitzelcloud', '#schnitzelmuc', '#schnitzels', '#schnitzelffm', '#schnitzelminga'])
