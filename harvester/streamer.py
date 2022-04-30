import tweepy as tw
import json
import couchdb

from util import get_sentiment, create_or_connect_db, couchify_tweet
from harvester_config import COUCHDB_ADDRESS

class StreamListener(tw.StreamListener):
    def __init__(self, keywords_dict, sentiment_analyzer, database):
        self.keywords_dict = keywords_dict
        self.sentiment_analyzer = sentiment_analyzer
        self.database = database
        pass

    def on_data(self, data):
        """
        When you stream by filter
        method goes here.
        """
        tweets = json.loads(data)
        print(f"tweet id: {tweets['id']}")
        tweets['electric_car'] = 0
        tweets['recycling'] = 0
        tweets['solar'] = 0

        if tweets['truncated'] == True:
            tweet = tweets['extended_tweet']['full_text']
        else:
            tweet = tweets['text']

        # Calculate sentiment
        sentiment_label, sentiment_prob = get_sentiment(self.sentiment_analyzer, tweet)
        tweets['sentiment_label'] = sentiment_label
        tweets['sentiment_prob'] = sentiment_prob
        print(f"    {tweets['sentiment_label']}: {tweets['sentiment_prob']}")

        # read and filter data by keywords
        for topic in self.keywords_dict.keys():
            keywords = self.keywords_dict[topic]
            if any(word in tweet for word in keywords):    
                tweets[topic] = 1

        # put into database
        # 'couchify' tweet. eg. add '_id' key that has same value as the tweet 'id'. For preventing duplicate tweets in the db.
        tweets_couchified = couchify_tweet(tweets)        
        print('    uploading on couchdb')
        self.database.save(tweets_couchified)
        print('    upload completed')

    def on_error(self, status_code):
        """
        Catching errors
        """
        print("Error", status_code)
        return
