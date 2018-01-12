# Twitter-mining-and-Tweet-Prediction
Taps into the Twitter api and dowloads up to 3200 tweets from any user, extracts the text from the tweet and trains it on a Markov chain model to produce an average tweet for that user

Markov chain code sourced from: https://github.com/G3Kappa/Adjustable-Markov-Chains

additional sources:
http://mike.teczno.com/notes/streaming-data-from-twitter.html
https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./



The main executable file is tweetuserdump.py

After downloading, imput your own twitter api credentials in their corresponding places

In lines 28 and 29 of tweetuserdump.py, edit the path location such that its specific to where the twitter mining folder resides on your computer

In line 104 of the same file, editing max_len changes the length of the outputed text

Feel free to edit the MaxTweets value on line 25 to anything you feel like.


#####################NOTE:###################################

Tweets greater than 140 characters will be cut off with an ellipsis, this will hopefully be resolved in future updates to this code.

