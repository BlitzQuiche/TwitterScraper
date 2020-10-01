import tweepy
import numpy
import pandas as pd
import time

# keys from twitter api page
consumer_key = "XXKRh8ZS63kd0vIWCZoiUgch6"
consumer_secret = "SH6hEXxGiBTTZHVFfFb1Ojm9EcyWWpvBNfC4ymGizXzFXhDzgO"

access_token = "2808799227-WwG5jpEe6Z4UdmGEnfA4ZKjUZpsMRYhO7wJikhg"
access_token_secret = "k5aCm7qEm9KUrhg2kFYjIFNl7JYw04pRTfttAWwEh2QDA"

#authentication and creating api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# creating list to store tweets 
data = []
# creating a stream listener that prints out tweet text on status
class MyStreamListener(tweepy.StreamListener):
	def __init__(self, time_limit=60):
		self.start_time = time.time()
		self.limit = time_limit
		super().__init__()

	def on_status(self, status):
		if (len(data) >= 1000):
			print("Max number of tweets reached!")
			return False
		if (time.time() - self.start_time) < self.limit:
			data.append([status.user.screen_name, status.text])
			print("Number of tweets: " +str(len(data)))
			return True
		else:
			return False


# creating the stream
mylistener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = mylistener)
print("Stream Created")

#
track = input("What word would you like to track?\n")

# starting the stream
print("Starting stream")
myStream.filter(track=[track])
print("Time limit exceeded: Ending stream")

# taking data and creating a dataframe from it
print("printing dataframe")
df = pd.DataFrame(data = data, columns = ["Name", "Tweet_Text"])
print(df)
df.to_csv('data.csv', index= False, encoding='utf-8')
print("exported to csv")