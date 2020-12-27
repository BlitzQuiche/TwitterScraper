import tweepy
# keys from twitter api page
consumer_key = "XXKRh8ZS63kd0vIWCZoiUgch6"
consumer_secret = "SH6hEXxGiBTTZHVFfFb1Ojm9EcyWWpvBNfC4ymGizXzFXhDzgO"

access_token = "2808799227-7tN8fkkdfmWRwz9SdbQbw5HLif9b8Ghsxve1leP"
access_token_secret = "bwqV0Z1QFeXFncpkF5uqKlfyo6kW2HiQIPeu4iXMTLIy3"

#authentication and creating api
#auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# dataframe to store tweets

# creating a stream listener that prints out tweet text on status
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print(status.text)

	def on_error(self, status_code):
		print("Error")
		print(status_code)
		if status_code == 420:
			return False


# creating the stream
mylistener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = mylistener)

# starting the stream
myStream.filter(track=['Python'])