import re

import tweepy
import translation
import verse
from urllib2 import urlopen


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : "" 
    }

  api = get_api(cfg)
  v = verse.get_verse()
  tweet = v[1] + translation.translate_to_converge(v[0],10)
  print tweet
  status = api.update_status(status=v[1]+' '+v[0])
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing


if __name__ == '__main__':
  main()
