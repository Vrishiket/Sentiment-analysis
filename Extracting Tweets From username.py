

#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Twitter API credentials
consumer_key = '12UCbopLPIyQ3S32G0bf6kNYX'
consumer_secret = '54KRYBa0gOUNxA0Ex1YWQqdTkyEL067MY7ed8ZC3j7kCELBLbt'
access_key = '4901534286-V4aGGswcis4xgK4VGZ5ns5lyjTJZtdDmmWRJ540'
access_secret = 'qR1QroqxEQW5kQTUaYNcZtPKDgkL3iYJdwudBgEsZishR'


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print( "getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print ("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	print (outtweets)
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
           word_tokens = word_tokenize(writer)  
           writer = csv.writer(f)
             
          
             writer.writerow(["id","created_at","text"])
             writerows(outtweets)
#	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("J_tsar")