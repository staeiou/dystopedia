import tweepy
import markovify
import wordfilter

# Tact function modified from function in cyberprefixer 
# (c) Molly White, 2013-2016, released MIT License
# https://github.com/molly/CyberPrefixer/blob/master/offensive.py

import offensive


# In[2]:

with open ("titles.txt", encoding="utf-8") as f:
    deltext = f.read()


# In[3]:

deletion_model = markovify.NewlineText(deltext)


# In[4]:

tweet = None
for i in range(10):
    title = deletion_model.make_short_sentence(130)
    if title is not None and not wordfilter.blacklisted(title) and offensive.tact(title):
        tweet = title


# In[5]:

if tweet is not None:
    print(tweet)


CONSUMER_KEY = twitter_login.CONSUMER_KEY
CONSUMER_SECRET = twitter_login.CONSUMER_SECRET
ACCESS_TOKEN = twitter_login.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = twitter_login.ACCESS_TOKEN_SECRET

# Authenticate

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status(tweet)
