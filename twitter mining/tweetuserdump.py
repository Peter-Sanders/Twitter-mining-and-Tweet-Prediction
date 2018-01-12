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



maxTweets = 3200 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
screen_name = input("User whos tweets are gathered: ")
pathlib.Path('/Users/Pete/OneDrive/Code/twitter mining/training_data/%s' % screen_name).mkdir(parents=True, exist_ok=True)
pathlib.Path('/Users/Pete/OneDrive/Code/twitter mining/stored_data/%s' % screen_name).mkdir(parents=True, exist_ok=True)
fName ='jsonfiles\\%s_tweets.txt' % screen_name# We'll store the tweets in a text file.
#fName ='%s_tweets.csv' % screen_name# We'll store the tweets in a csv file.
#fName ='%s_tweets.json' % screen_name# We'll store the tweets in a json file.


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


import json
tweets = []
for line in open(fName):
    try:
        tweets.append(json.loads(line))
    except:
        pass

texts = [tweet['text'] for tweet in tweets]

print("Tweet only file created called {0}_tweets_text.txt".format(screen_name))
out = open('training_data\\%s\\%s_tweets_text.txt' %(screen_name,screen_name), 'w', encoding = "utf-8")
out.write("\n".join(str(x) for x in texts))
out.close()




from markovchain import *
from training_algorithms import *

# Builds a formatted string from the generator
def gen(m):
    return ''.join([w for w in m.generate_formatted(word_wrap=60, soft_wrap=True, start_with=None, max_len=20, verbose=True)])

# Initialize the chain and train it on a few of my reddit posts.
mkv = MarkovChain()
mkv.bulk_train('training_data\\%s\\*.txt' %screen_name, verbose=True)
# Or,``
# mkv.load_training('training01.txt')

# Store this information for later, so that there's no need to re-train the next time.
mkv.save_training('stored_data\\%s\\training' %screen_name)
# Adjust the weights with the help of some fitness functions.
mkv.bulk_adjust_weights(fitness_functions=[aw_favor_alternating_complexity, aw_mul(aw_favor_punctuation, 0.5)],
                            iterations=10000,
                            verbose=True)
# Save the new state to a different file, to prevent feedback loops.
mkv.save_training('stored_data\\%s\\training01' %screen_name)
# Print a sample output after all weights have been adjusted.
print(gen(mkv))
