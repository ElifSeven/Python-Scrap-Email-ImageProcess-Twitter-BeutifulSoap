import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
# print(tweet.text)

# print(user.followers_count)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'asdf':
        follower.follow()
        break
    ##print(follower.name)
