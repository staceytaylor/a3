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

# Retrieves a Unique ID for a given user 
s = get_profile("CitronResearch")
print "Name:" +s.name
print "id:" +s.id_str

#Retrieves the most popular re-tweet from Citron Research
#t = get_tweets("Shopify")
#list = []
#for tweet in t:
#	list.append(tweet.retweet_count)
#for tweet in t:
#	if tweet.retweet_count == max(list):
#		text = tweet.text
#print "the most popular tweet of citron research is \"" +text+ "\" with a retweet count of "+str(max(list))



#Creates a list of Tweets from Shopify's official account that Mention Citron Research - NONE EXIST
def get_tweets(screen_name):

	alltweets = []
	try:
		tweets = api.user_timeline(screen_name, count=3200)
		print "tweets"
		alltweets.extend(tweets)
		oldest = alltweets[-1].id - 1
		print oldest
		print len(tweets)
		while len(tweets) > 0:
			tweets = api.user_timeline(screen_name, count=3200, max_id=oldest)
			alltweets.extend(tweets)
			oldest = alltweets[-1].id - 1
			print "...%s tweets downloaded so far" % (len(alltweets))
	except:
		user_profile = "broken"
	return alltweets


# profiles = ["CitronResearch","Shopify"]
# with open ('tweets.csv', 'wb') as outfile:
#	writer = csv.writer(outfile)
#	writer.writerow (["id", "user", "created_at", "text"])
#	for profile in profiles:
#		t = get_tweets(profile)
#		for tweet in t:
#			writer.writerow([tweet.user.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])


list1 = []
t = get_tweets("CitronResearch")  
for tweet in t:
    list1.append(tweet.retweet_count)

for tweet in t:
    if tweet.retweet_count == max(list1):
        text1 = tweet.text

with open ('tweets.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    for tweet in t:
        if "FTC" in tweet.text:
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
#    t2 = get_tweets("Shopify")
#    for tweet in t2:
#        if "citron" in tweet.text:
#            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
#print "most popular tweet of citron research is: \"" + text1 + " \" with a retweet count of " +str(max(list1))

