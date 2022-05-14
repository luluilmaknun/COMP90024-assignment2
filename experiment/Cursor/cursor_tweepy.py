# -*- coding: utf-8 -*-
"""Cursor Tweepy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ltKU1Mw4TwwU6VWAPgqsMc6kaWs42aJZ
"""

LOCATIONS = {}
LOCATIONS["west"] = [144.317, -38.0, 144.856, -37.166]
LOCATIONS["north"] = [144.856, -38.0, 145.185, -37.166]
LOCATIONS["east"] = [145.185, -38.0, 145.901, -37.166]
LOCATIONS["south"] = [144.655, -38.533, 145.901, -38.0]

keywords_electriccar = ["drive electric", "electric future", "electric car", "electric vehicle", "modelx", "ev conversion",
    "elon musk", "tesla ", "tesla life", "tesla car", "tesla roadster", "tesla motors", "tesla model",
    "car charger", "self driving", "urban mobility", "zero emissions", "electric mobility", "emobility",
    "self driving car", "autonomous vehicle", "autonomous car", "future car", "ev sales", "ev battery",
    "autonomous driving", "audietron", "alternative fuel", "connected vehicle", "connected car",
    "mahindra"]

keywords_recycling = [
    'reuse', 'waste', 'composting', 'landfill', 'conserve', 'receptacles', 'disposal', 'recycle',
    'biodegradable', 'yellow bin', 'e-waste', 'reusable', 'reprocessing', 'recycled', 'recyclebots',
    'waste paper', 'carbon neutral', 'reduce']

keywords_solar = [
     'solar', 'solar panels', 'solar battery', 'csp', 'renewable energy', 'elon musk', 
        'sun power', 'photovoltaic', 'cell', 'wind turbine', 'hydro', 'solar city', 'windmill',
         'green energy', 'geothermal', 'biomass', 'carbon tax', 'carbon policy', 'C02 footprint', 
         'EBITDA', 'Enova', 'Diamond Energy', 'Momentum Energy', 'Aurora Energy', 'Tilt', 'WestWind',
         'FinnBiogas', 'biogas', 'Acciona'                 
]

config = {
    "AUTH": {
        "CONSUMER_KEY": "mxqyJYQQTjK8GELo7WuyF7PZL",
        "CONSUMER_KEY_SECRET": "GCoiXIGJhixATDaGJPxnRsDAl8wkRFFSGPCQkZdeproCIrfKCV",
        "ACCESS_TOKEN": "1514125532824502275-aGDxWMrxR4Qc1FCip9rxOww7vnGrQu",
        "ACCESS_TOKEN_SECRET": "VY74YrL3o9T48nxM5i4lBKajESQxtX6WYFUlETUYKR2HT",
    },
    "KEYWORDS": {
        'electric_cars': keywords_electriccar,
        'recycling': keywords_recycling,
        'solar': keywords_solar,
    },
    "LOCATIONS":LOCATIONS
}

# add #keywords as well to keywords list
keywords_dict = {}
for topic in ('electric_cars', 'recycling', 'solar'):
    keywords = []
    for keyword in config["KEYWORDS"][topic]:
        hash = "#"
        for word in keyword.split(" "):
            hash += word
        keywords.append(hash)
    keywords += config["KEYWORDS"][topic]
    keywords_dict[topic] = keywords

import tweepy as tw
import json

from pysentimiento import create_analyzer

# Connect to API stream
auth = tw.OAuthHandler(config["AUTH"]["CONSUMER_KEY"], 
                           config["AUTH"]["CONSUMER_KEY_SECRET"])
auth.set_access_token(config["AUTH"]["ACCESS_TOKEN"], 
                      config["AUTH"]["ACCESS_TOKEN_SECRET"])
api = tw.API(auth, wait_on_rate_limit=True)

# Setup sentiment analyzer
sentiment_analyzer = create_analyzer(task="sentiment", lang="en")

import time
from pysentimiento.preprocessing import preprocess_tweet

# run sentiment analysis on text data
def get_sentiment(sentiment_analyzer, tweet_text):
    content = preprocess_tweet(tweet_text)
    try:
        sentiment = sentiment_analyzer.predict(content)
    except:
        pass
    # return sentiment label (POS/NEU/NEG) and probability (softmax output)
    return sentiment.__dict__['output'], max(sentiment.__dict__['probas'].values())


# Helper function for handling pagination in our search and handle rate limits
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tw.RateLimitError:
            print('Reached rate limite. Sleeping for >15 minutes')
            time.sleep(15 * 61)
        except StopIteration:
            break


import os
import json
import argparse

import couchdb

# exclude '_rev' key in tweet_json and
# make '_id' key if it doesn't exist (couchdb looks for '_id' for document key) -> tweet id as db key prevents duplicates

def couchify_tweet(tweet_json):
    keys_to_exclude = ["_rev"]
    json_couchified = {key: tweet_json[key] for key in tweet_json.keys() if key not in keys_to_exclude}
    if "_id" not in json_couchified:
        json_couchified["_id"] = str(json_couchified["id"])
    return json_couchified


def create_or_connect_db(couchserver, db_name):
    if db_name in couchserver:
        db = couchserver[db_name]
    else:
        db = couchserver.create(db_name)
    return db


# Function to search tweets based on keywords
def search_tweets(api, db, keywords_list, locations, sentiment_analyzer):
    for direction, loc in locations.items():
        # Connect to DB
        db_name = f"twitter_{direction}"
        db = create_or_connect_db(couchserver=couchserver,
                            db_name = db_name)
        print(db)
        
        # Get centre, assuming that earth is flat :))))
        lon = (loc[0] + loc[2])/2
        lat = (loc[1] + loc[3])/2

        # Get radius, assuming that 1 unit is 111 km
        diff = min(lon - loc[0], lat - loc[1])
        radius = round(diff * 111)

        # Geocode
        geocode = f"{lat},{lon},{radius}km"
        print(direction, geocode)

        # Seach and save to files
        for topic, keywords in keywords_list.items():
            with open("%s_cursor_%s.json" % (direction, topic), "w+") as f:
                result = {"total": 0, "items": []}
                for keyword in keywords:
                    query = keyword + ' -filter:retweets'
                    tweets = limit_handled(tw.Cursor(api.search, 
                                                      q=query,
                                                      tweet_mode='extended',
                                                      lang='en',
                                                      geocode=geocode).items())

                    for tweet in tweets:
                        result_json = tweet._json
                        # result_json['direction'] = direction
                        result_json['solar'] = 1 if topic == 'solar' else 0
                        result_json['recycling'] = 1 if topic == 'recycling' else 0
                        result_json['electric_cars'] = 1 if topic == 'electric_cars' else 0

                        sentiment_label, sentiment_prob = get_sentiment(sentiment_analyzer, result_json['full_text'])
                        result_json['sentiment_label'] = sentiment_label
                        result_json['sentiment_prob'] = sentiment_prob
                        print(direction, result_json['solar'], result_json['recycling'], result_json['electric_cars'], \
                            result_json['sentiment_label'], result_json['sentiment_prob'])

                        result["items"].append(result_json)
                        try:
                            tweets_couchified = couchify_tweet(result_json)
                            print('    uploading on couchdb')
                            db.save(tweets_couchified)
                            print('    upload completed')
                        except couchdb.http.ResourceConflict:
                            pass

                result["total"] = len(result["items"])
                json.dump(result, f)

            print(direction, topic, len(result["items"]))

if __name__ == "__main__":
    COUCHDB_ADDRESS = "http://dev:dev@172.26.131.7:5984/"
    # Couchdb. Need to have unimelb vpn active
    couchserver = couchdb.Server(COUCHDB_ADDRESS)
    print('\n', couchserver)

    search_tweets(api, couchserver, keywords_dict, config["LOCATIONS"], sentiment_analyzer)
