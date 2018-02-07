#!/usr/local/bin/python

from tweet_mine import *
from write_tweet import *
from gtts import gTTS
import os




print("User whos tweets are gathered")
screen_name = input('>>> ')

print("Have you downloaded %s's tweets before y/n? " % screen_name)
q1 = input('>>> ')
if q1 == 'n':
    tweet_mine(screen_name)
print("Have you trained the Markov Chain yet y/n?")
q2 = input('>>> ')
if q2 == 'n':
    train_chain(screen_name)
print("Sample tweet y/n? ")
q3 = input(">>> ")
if q3 == 'y':
    tweet = write_tweets(screen_name)
    print(tweet)
print("Save how many tweets ?")
q4 = int(input('>>> '))
if q4 == 0:
    pass
else:
    save_tweets(screen_name, q4)

print('Speak tweet y/n?')
q5 = input('>>> ')
if q5 == 'y':
    if q3 != 'y':
        tweet = write_tweets(screen_name)
    else:
        pass
    lang = 'en'
    speech = gTTS(text=tweet, lang=lang, slow=False)
    speech.save("%s_speech.mp3" % screen_name)
    os.system('%s_speech.mp3' % screen_name)
else:
    pass



