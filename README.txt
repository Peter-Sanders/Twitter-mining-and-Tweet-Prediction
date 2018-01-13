# Twitter-mining-and-Tweet-Prediction
Taps into the Twitter api and dowloads up to 3200 tweets from any user, extracts the text from the tweet and trains it on a Markov chain model to produce an average tweet for that user

Markov chain code sourced from: https://github.com/G3Kappa/Adjustable-Markov-Chains

additional sources:
http://mike.teczno.com/notes/streaming-data-from-twitter.html
https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./
https://gist.github.com/timothyrenner/dd487b9fd8081530509c



The main executable file is use.py

After downloading, imput your own twitter api credentials in their corresponding places

In lines 33 and 34 of tweet_mine.py, edit the path location such that its specific to where the twitter mining folder resides on your computer

Feel free to edit the MaxTweets value on line 25 to anything you feel like.

Edit the max_len value on line 7 of write_tweet.py to change the length of the tweet


#####################NOTE:###################################

Tweets greater than 140 characters will be cut off with an ellipsis, this will hopefully be resolved in future updates to this code.

