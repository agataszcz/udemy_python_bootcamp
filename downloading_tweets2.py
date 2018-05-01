#!/usr/bin/env python
'''Downloading tweets to a JSON-Lines file (one tweet(status) per line). Using pagination'''

import tweepy
from tweepy import Cursor
import json

#register on https://apps.twitter.com/ to get your Twitter API credentials

#save your Twitter API credentials
consumer_key = "myconsumerkey"
consumer_secret = "myconsumersecret"
access_key = "myaccesskey"
access_secret = "myaccesssecret"


def download_tweets(screen_name):
	#one can download approx. 3240 most recent tweets of a particular user
	
	#get an authorization and create an API instance
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#write tweets(statuses) to a JSONL file (one tweet per line)
	filename = "{}_user_timeline.jsonl".format(screen_name)
	
	with open(filename, 'w') as f:
		#specify how many items per page you want
		for page in Cursor(api.user_timeline, screen_name=screen_name, count=200).pages(16):
			for status in page:
				f.write(json.dumps(status._json)+"\n")


if __name__ == "__main__":
	download_tweets(screen_name="JohnDoe")
	#input the screen name of a user, whose tweets you would like to download

