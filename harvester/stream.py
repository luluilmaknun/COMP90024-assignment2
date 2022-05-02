import tweepy as tw
import json
from pysentimiento import create_analyzer
import couchdb
import argparse

from streamer import StreamListener
from transformers import pipeline
from harvester_config import AUTH, KEYWORDS, LOCATIONS, COUCHDB_ADDRESS
from util import create_or_connect_db

############################# ENSURE VPN IS ENABLED (if you want to run locally) ###############################

# parse args
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-r", "--region", required=True, type=str, help="type region in lower case")
args = arg_parser.parse_args()
search_region = args.region
search_box = LOCATIONS[f"{search_region}"]
print(f'\nSearch region is "{search_region}" with bounding box {search_box}...')

# add #keywords as well to keywords list
keywords_dict = {}
for topic in ('electric_cars', 'recycling', 'solar'):
    keywords = []
    for keyword in KEYWORDS[topic]:
        hash = "#"
        for word in keyword.split(" "):
            hash += word
        keywords.append(hash)
    keywords += KEYWORDS[topic]
    keywords_dict[topic] = keywords

# Sentiment Analysis model
print('\nLoad sentiment analyzer, may take >10 sec...')
sentiment_analyzer = create_analyzer(task="sentiment", lang="en")

# Connect to API stream
auth = tw.OAuthHandler(AUTH[search_region]["CONSUMER_KEY"], 
                       AUTH[search_region]["CONSUMER_KEY_SECRET"])
auth.set_access_token(AUTH[search_region]["ACCESS_TOKEN"], 
                      AUTH[search_region]["ACCESS_TOKEN_SECRET"])
api = tw.API(auth, wait_on_rate_limit=True)

# Couchdb. Need to have unimelb vpn active
couchserver = couchdb.Server(COUCHDB_ADDRESS)
print('\n', couchserver)
db_name = f"twitter_{search_region}"
db = create_or_connect_db(couchserver=couchserver,
                          db_name = db_name)
print(db)

# Stream
mystream_listener = StreamListener(keywords_dict=keywords_dict,
                                   sentiment_analyzer=sentiment_analyzer,
                                   database = db)
mystream = tw.Stream(auth=api.auth, listener=mystream_listener)

# Filter twitter
print("\nStart streaming...")
mystream.filter(languages = ["en"], 
                locations=search_box)
