import tweepy as tw
import json
from pysentimiento import create_analyzer
import couchdb

from streamer import StreamListener
from transformers import pipeline
from harvester_config import AUTH, KEYWORDS, LOCATIONS, COUCHDB_ADDRESS
from util import create_or_connect_db

# Read configuration
keywords = []
for keyword in KEYWORDS:
    hash = "#"
    for word in keyword:
        hash += word
    keywords.append(hash)
keywords += KEYWORDS

# Sentiment Analysis model
print('\nLoad sentiment analyzer...')
sentiment_analyzer = create_analyzer(task="sentiment", lang="en")

# Connect to API stream
auth = tw.OAuthHandler(AUTH["CONSUMER_KEY"], 
                       AUTH["CONSUMER_KEY_SECRET"])
auth.set_access_token(AUTH["ACCESS_TOKEN"], 
                      AUTH["ACCESS_TOKEN_SECRET"])
api = tw.API(auth, wait_on_rate_limit=True)

# Couchdb. Need to have unimelb vpn active
couchserver = couchdb.Server(COUCHDB_ADDRESS)
print('\n', couchserver)
db = create_or_connect_db(couchserver=couchserver,
                          db_name = "twitter")
print(db)

# Stream
mystream_listener = StreamListener(keywords=KEYWORDS,
                                   sentiment_analyzer=sentiment_analyzer,
                                   database = db)
mystream = tw.Stream(auth=api.auth, listener=mystream_listener)

# Filter twitter
print("\nStart streaming...")
mystream.filter(languages = ["en"], 
                locations=LOCATIONS)
