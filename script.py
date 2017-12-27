import tweepy
from textblob import TextBlob

consumer_key = 'LsuODLkhMOuAeemlxdzCuCJzX'
consumer_secret = 'pbrnWP0TRTW3lcrfu5c8qnr4GuRUKoRFMLFyQu04jwXskZozNE'

access_token = '1533962989-TeeRTMwI7coW8N53O4mhqFKvOfJ6OSQScFPgpKm'
access_token_secret = 'duF5lMsu6QPrrS3m0CvOoSKTnxLzcK5D6z66FNFuAqkmW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Taxes')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
