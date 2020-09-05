
import tweepy


#Twitter credentials for the app
consumer_key    = 'XXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXX'
access_key      = 'XXXXXXXXXXXxx'
access_secret   = 'XXXXXXXXXXXXx'


#pass twitter credentials to tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


url      = "https://twitter.com/andrewyng/status/1290029141522173952?s=21"
name     = url.split("/")[3]
tweet_id = url.split("/")[-1].split('?')[0]


replies  =  []
for tweet in tweepy.Cursor(api.search,q=name, result_type='recent', timeout=999999).items(100):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet)


for i in replies:
    print(i.text)