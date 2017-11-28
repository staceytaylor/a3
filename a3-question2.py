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


s = get_profile("CitronResearch")
print "Name:" +s.name
print "id:" +s.id_str

t = get_tweets("CitronResearch")
list = []
for tweet in t:
	list.append(tweet.retweet_count)
for tweet in t:
	if tweet.retweet_count == max(list):
		text = tweet.text


print "the most popular tweet of citron research is \"" +text+ "\" with a retweet count of "+str(max(list))
## profiles = ["CitronResearch", "Shopify"]

## with open ('tweets.csv', 'wb') as outfile:
##	writer = csv.writer(outfile)
##	writer.writerow (["id", "user", "created_at", "text"])
##	for profile in profiles:
##		t = get_tweets(profile)
##		for tweet in t:
##			writer.writerow([tweet.user.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
			

