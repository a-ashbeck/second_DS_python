# Import tweepy, which interfaces with the Twitter API
import tweepy
# Import textblo, which offers text analysis tools
from textblob import TextBlob

# Twitter API access keys and tokens
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Setting tweepy up with API access info
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Setting the search term
public_tweets = api.search('Taxes')

# Loop to grap tweets and analyze text
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.tags)
    print(analysis.words)
    print(analysis.sentiment)
