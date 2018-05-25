# Dependencies
import tweepy
import time
import json
from random import randint
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

quotes = ["a", "b", "c"]

# Create a function that tweets

def TweetOut(a):
    api.update_status(quotes[a])


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinite loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(10)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1