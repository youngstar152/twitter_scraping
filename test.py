import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み
import tweepy

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
#twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理
auth = tweepy.OAuthHandler(CK, CS) # Twitter API認証
auth.set_access_token(AT, ATS) # アクセストークン設定
api = tweepy.API(auth) 

#タイムライン取得
#result = api.home_timeline(count=1)
tweets = api.search_tweets(q = "スパイファミリー OR SPY×FAMILY -retweets -http -RT -filter:retweets -filter:links",lang='ja',count=10)

for tweet in tweets:
    print('='*80)
    #print('ツイートID : ', tweet.id)
    #print('ツイート時間 : ', tweet.created_at)
    print('ツイート本文 : ', tweet.text)
    print('ユーザ名 : ', tweet.user.name) 
    #print('スクリーンネーム : ', tweet.user.screen_name) 
    #print('フォロー数 : ', tweet.user.friends_count) 
    #print('フォロワー数 : ', tweet.user.followers_count) 
    #print('概要 : ', tweet.user.description) 
    #print('='*80)