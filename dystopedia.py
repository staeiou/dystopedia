import random
import twitter_login
import tweepy
import markovify
import wordfilter

# Tact function modified from function in cyberprefixer 
# (c) Molly White, 2013-2016, released MIT License
# https://github.com/molly/CyberPrefixer/blob/master/offensive.py

import offensive


# In[2]:

with open ("/home/staeiou/bots/dystopedia/titles.txt", encoding="utf-8") as f:
    deltext = f.read()

deltext = deltext.replace(".", " ")
deltext = deltext.encode('ascii', 'ignore').decode('ascii')
# In[3]:

deletion_model = markovify.NewlineText(deltext)


# In[4]:

tweet = None
tweets = []
for i in range(250):
    title = deletion_model.make_short_sentence(90)
    if title is not None and not wordfilter.blacklisted(title) and offensive.tact(title):
        tweets.append(title)

tweets = sorted(tweets, key=len, reverse=True)
rand_num = random.randrange(0,25)

# In[5]:

if tweets[rand_num] is not None:
    print(tweets[rand_num])


CONSUMER_KEY = twitter_login.CONSUMER_KEY
CONSUMER_SECRET = twitter_login.CONSUMER_SECRET
ACCESS_TOKEN = twitter_login.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = twitter_login.ACCESS_TOKEN_SECRET

# Authenticate

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status(tweets[rand_num])
