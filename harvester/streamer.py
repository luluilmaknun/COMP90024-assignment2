import tweepy as tw
import json

from util import get_sentiment


class StreamListener(tw.StreamListener):
    def __init__(self, keywords, sentiment_pipeline):
        self.keywords = keywords
        self.sentiment_pipeline = sentiment_pipeline
        pass

    def on_data(self, data):
        """
        When you stream by filter
        method goes here.
        """
        tweets = json.loads(data)
        tweets['electric_car'] = 0

        if tweets['truncated'] == True:
            tweet = tweets['extended_tweet']['full_text']
        else:
            tweet = tweets['text']

        # Calculate sentiment
        sentiment = get_sentiment(self.sentiment_pipeline, tweet)
        tweets['sentiment'] = sentiment['sentiment']

        # read and filter data by keywords
        if any(word in tweet for word in self.keywords):    
            tweets['electric_car'] = 1

        # put into database
        ## TODO

        return True

    def on_error(self, status_code):
        """
        Catching errors
        """
        print("Error", status_code)
        return
