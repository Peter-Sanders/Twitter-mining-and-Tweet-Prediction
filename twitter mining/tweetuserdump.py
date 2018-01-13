#!/usr/bin/env python

import tweepy

consumer_key = "****"
consumer_secret = "****"
access_key = "****"
access_secret = "****"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)



import sys
import jsonpickle
import os
import csv
import pathlib
from markovchain import *
from training_algorithms import *
from tweet_utils import*
import json

def tweet_mine(screen_name):


    maxTweets = 1000 # Some arbitrary large number
    tweetsPerQry = 100  # this is the max the API permits
    pathlib.Path('/your file path/twitter mining/training_data/%s' % screen_name).mkdir(parents=True, exist_ok=True)
    pathlib.Path('/your file path/twitter mining/stored_data/%s' % screen_name).mkdir(parents=True, exist_ok=True)
    fName ='jsonfiles\\%s_tweets.txt' % screen_name# We'll store the tweets in a text file.


    # If results from a specific ID onwards are reqd, set since_id to that ID.
    # else default to no lower limit, go as far back as API allows
    sinceId = None

    # If results only below a specific ID are, set max_id to that ID.
    # else default to no upper limit, start from the most recent tweet matching the search query.
    max_id = 0

    tweetCount = 0
    print("Downloading max {0} tweets".format(maxTweets))
    with open(fName, 'w') as f:
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):

                        new_tweets = api.user_timeline(screen_name = screen_name,count=tweetsPerQry,
                        include_rts = False, exclude_replies = True)
                    else:
                        new_tweets = api.user_timeline(screen_name = screen_name,count=tweetsPerQry,
                        include_rts = False, exclude_replies = True, since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = api.user_timeline(screen_name = screen_name,count=tweetsPerQry,
                        include_rts = False, exclude_replies = True, max_id=str(max_id - 1))
                    else:
                        new_tweets = api.user_timeline(screen_name = screen_name,count=tweetsPerQry,
                        include_rts = False, exclude_replies = True, max_id=str(max_id - 1),
                        since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                   f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                           '\n')
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break

    print ("Downloaded {0} tweets, Saved to {1} in json format".format(tweetCount, fName))


    tweets = []
    for line in open(fName):
        try:
            tweets.append(json.loads(line))
        except:
            pass

    texts = [get_text_cleaned(tweet) for tweet in tweets]
    texts = [get_text_sanitized(tweet) for tweet in tweets]




    print("Tweet only file created called {0}_tweets_text.txt".format(screen_name))
    out = open('training_data\\%s\\%s_tweets_text.txt' %(screen_name,screen_name), 'w', encoding = "utf-8")
    out.write("\n".join(str(x) for x in texts))
    out.close()
