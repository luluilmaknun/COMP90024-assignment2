import tweepy as tw
import json


class StreamListener(tw.StreamListener):
    def __init__(self, keywords):
        self.keywords = keywords
        pass

    def on_data(self, data):
        """
        When you stream by filter
        method goes here.
        """
        tweets = json.loads(data)

        # read and filter data by keywords
        if any(word in tweets['text'] for word in self.keywords):
            created_at = tweets['created_at']
            coordinates = tweets['coordinates']
            place = tweets['place']
            if 'extended_tweet' in tweets:
                tweet = tweets['extended_tweet']['full_text']
            else:
                tweet = tweets['text']

        # preprocess data
        ## TODO

        # put into database
        ## TODO

        return True

    def on_error(self, status_code):
        """
        Catching errors
        """
        print("Error", status_code)
        return
