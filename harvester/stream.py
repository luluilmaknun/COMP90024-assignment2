import tweepy as tw
import json
from pysentimiento import create_analyzer

from streamer import StreamListener
from transformers import pipeline
from harvester_config import AUTH, KEYWORDS, LOCATIONS


# Read configuration
keywords = []
for keyword in KEYWORDS:
    hash = "#"
    for word in keyword:
        hash += word
    keywords.append(hash)
keywords += KEYWORDS

# Sentiment Analysis model
print('Load sentiment analyzer...')
sentiment_analyzer = create_analyzer(task="sentiment", lang="en")

# Connect to API stream
auth = tw.OAuthHandler(AUTH["CONSUMER_KEY"], 
                       AUTH["CONSUMER_KEY_SECRET"])
auth.set_access_token(AUTH["ACCESS_TOKEN"], 
                      AUTH["ACCESS_TOKEN_SECRET"])
api = tw.API(auth, wait_on_rate_limit=True)

# Stream
mystream_listener = StreamListener(keywords=KEYWORDS,
                                   sentiment_analyzer=sentiment_analyzer)
mystream = tw.Stream(auth=api.auth, listener=mystream_listener)

# Filter twitter
print("Start streaming...")
mystream.filter(languages = ["en"], 
                locations=LOCATIONS)
