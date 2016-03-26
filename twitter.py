import re
import breakup
import tweepy
import translation
import verse
import textblob
from urllib2 import urlopen


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def tweet(text, api):
  tweets = breakup.split_tweet(text)
  for tweet in reversed(tweets):
    api.update_status(status=tweet)

def main():
  # Fill in the values noted in previous step here
  f = open('keys.txt','r')
  cfg = {}
  cfg_keys = ["consumer_key", "consumer_secret", "access_token" , "access_token_secret"]

  for i in range(0,4):
      l = f.readline().strip()
      cfg[cfg_keys[i]] = l

  api = get_api(cfg)
  t1 = ''
  t2 = ''  
  while True:
    try:
      v = verse.get_verse()
      t1 = v[1] + v[0]
      t2 = v[1] + ' ' + translation.translate_to_converge(v[0],10) 
      break
    except textblob.exceptions.NotTranslated:
      print "translator failure"

  tweet(t1, api)
  tweet(t2, api)

if __name__ == '__main__':
  main()
