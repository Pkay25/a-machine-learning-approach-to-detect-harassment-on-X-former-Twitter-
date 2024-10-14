import tweepy
import sys


def get_tweets(name, number):

    twitter_keys = open('Tweeter_Keys.txt', 'r').read().splitlines()
    api_key = twitter_keys[0]
    api_key_secret = twitter_keys[1]
    access_token = twitter_keys[2]
    access_token_secret = twitter_keys[3]

    auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
    auth_handler.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth_handler)

    posts = api.user_timeline(screen_name=name, count=number, lang="en", tweet_mode="extended")

    posts_text = []
    for tweet in posts:
        posts_text.append(tweet.full_text)

    return posts_text

