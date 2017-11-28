#Twitter API 

import tweepy, time, csv

#Twitter API credentials

consumer_key = "xHxN9CmFsFcH4kME9LVUh2v6l"
consumer_secret = "bvMG55mYtHCpdok174GDflEzKirsOpnGtem3YetmbGqLyzlZAE"
access_key = "1375777406-1lo4y9pq1sH5XLjqQSBHKYezwBBWOhXUPuH9OC3"
access_secret = "SGWe4TFIWTKVJjdOhDfLlADEXWm8xIPU4TFRlHkKMIPGC"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#collects a Twitter profile reflect and returns a Twitter object

def get_profile(screen_name):
	try:
		user_profile = api.get_user(screen_name)
	except:
		user_profile = "broken" 
	return user_profile

# Step 1: Retrieves the unique ID for a given Twitter user	
#s = get_profile("CitronResearch")
#print "Name:" +s.name
#print "id:" +s.id_str
	
def get_tweets(screen_name):
	try:
		tweets = api.user_timeline(screen_name = screen_name,count = 20)
	except:
		tweets = "broken"
	return tweets


s = get_profile("CitronResearch")  # Do this for Citron and Shopify (and Tobi later for the other question)
print "Name:" +s.name
print "id:" +s.id_str
