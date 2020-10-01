import tweepy
import numpy
import pandas as pd

# keys from twitter api page
consumer_key = "XXKRh8ZS63kd0vIWCZoiUgch6"
consumer_secret = "SH6hEXxGiBTTZHVFfFb1Ojm9EcyWWpvBNfC4ymGizXzFXhDzgO"

access_token = "2808799227-WwG5jpEe6Z4UdmGEnfA4ZKjUZpsMRYhO7wJikhg"
access_token_secret = "k5aCm7qEm9KUrhg2kFYjIFNl7JYw04pRTfttAWwEh2QDA"

#authentication and creating api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# dataframe to store tweets


# creating a stream listener that prints out tweet text on status
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print(status.text)


# creating the stream
mylistener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = mylistener)

# starting the stream
myStream.filter(track=['python'])