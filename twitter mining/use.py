from tweet_mine import *
from write_tweet import *




screen_name = input("User whos tweets are gathered: ")

q1 = input("Have you downloaded %s's tweets before y/n? ")

if q1 == 'n':
    tweet_mine(screen_name)

else:
    print("Understood")




ask = input("Write tweet y/n? ")

if ask == 'y':

    write_tweet(screen_name)

else:

    print("Finished")
