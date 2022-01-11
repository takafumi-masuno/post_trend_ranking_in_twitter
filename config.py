import tweepy
import os
from dotenv import load_dotenv

# .envファイルを読み込み
load_dotenv()

# 認証に必要なキーとトークン
CONSUMER_KEY    = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN    = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET   = os.getenv('ACCESS_SECRET')

# APIの認証
def twitter_api():
    auth            = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    tweepy.API(auth)

