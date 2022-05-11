from ast import Param
from inspect import Parameter
import couchdb

from flask_cors import CORS
from flask import Flask, jsonify
from flask_restful import Resource, Api
from couchdb_config import DB_URI, DB_LIST
from util import *


app = Flask(__name__)
api = Api(app)
CORS(app)


class Tweet(Resource):
    def get(self):
        # Function to return all documents from databases
        print("Entering database")
        output = []

        # Iterating through list of databases
        for db_name in DB_LIST:
            db = couch[db_name]
            rows = db.view('_all_docs', include_docs=True)
            data = [row['doc'] for row in rows]
            output += data

        return jsonify(
            total=len(output),
            rows=output
        )

# Function to return data from north melbourne databases and aurin data


class TweetOfNorth(Resource):
    def get(self):
        print("Entering database")
        # get the related aurin data
        aurin_result = get_aurin(search_by="region", search_region="north")
        test = []

        # query couchdb view to get the related data
        db_name = 'twitter_north'
        if db_name in DB_LIST:
            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey',
                           reduce=True, group=True, group_level=2)
            for item in rows:
                result = {}
                result["key"] = item.key
                result["value"] = item.value
                test.append(result)

        return jsonify(output=test, aurin=aurin_result)

# Function to return data from south melbourne databases and aurin data


class TweetOfSouth(Resource):
    def get(self):
        print("Entering database")
        # get the related aurin data
        aurin_result = get_aurin(search_by="region", search_region="south")
        test = []

        # query couchdb view to get the related data
        db_name = 'twitter_south'
        if db_name in DB_LIST:
            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey',
                           reduce=True, group=True, group_level=2)
            for item in rows:
                result = {}
                result["key"] = item.key
                result["value"] = item.value
                test.append(result)

        return jsonify(output=test, aurin=aurin_result)

# Function to return data from west melbourne databases and aurin data


class TweetOfWest(Resource):
    def get(self):
        print("Entering database")
        # get the related aurin data
        aurin_result = get_aurin(search_by="region", search_region="west")
        test = []

        # query couchdb view to get the related data
        db_name = 'twitter_west'
        if db_name in DB_LIST:
            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey',
                           reduce=True, group=True, group_level=2)
            for item in rows:
                result = {}
                result["key"] = item.key
                result["value"] = item.value
                test.append(result)

        return jsonify(output=test, aurin=aurin_result)

# Function to return data from east melbourne databases and aurin data


class TweetOfEast(Resource):
    def get(self):
        print("Entering database")
        # get the related aurin data
        aurin_result = get_aurin(search_by="region", search_region="east")
        test = []

        # query couchdb view to get the related data
        db_name = 'twitter_east'
        if db_name in DB_LIST:
            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey',
                           reduce=True, group=True, group_level=2)
            for item in rows:
                result = {}
                result["key"] = item.key
                result["value"] = item.value
                test.append(result)

        return jsonify(output=test, aurin=aurin_result)

# Function to return data on recycling in all regoin of melbourne from couchdb views and aurin data


class TweetsOnRecycling(Resource):
    def get(self):
        print("Entering database")
        # get the related aurin data
        # aurin_result = get_aurin(search_by="topic", search_topic="recycling")
        test = []
        regions = []
        labels = []

        # query couchdb view to get the related data
        for db_name in DB_LIST:
            if db_name in ["twitter_north", "twitter_east", "twitter_west", "twitter_south"]:
                region = db_name.split("_")[1]
            else:
                continue

            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey',
                           reduce=True, group=True, group_level=2)

            for item in rows:
                curent_key = item.key
                if(curent_key[0] == 'recycling'):
                    label = curent_key[1]
                    result = {}

                    if region not in regions:
                        regions.append(region)
                        result["region"] = region

                    if label == "NEG":
                        labels.append(label)
                        result["NEG"] = item.value
                    elif label == "NEU":
                        labels.append(label)
                        result["NEU"] = item.value
                    elif label == "POS":
                        labels.append(label)
                        result["POS"] = item.value
                    else:
                        continue

                    if 'region' not in result.keys():
                        for i in test:
                            if(i['region'] == region):
                                i[label] = item.value
                                continue
                    else:
                        test.append(result)

            test = compute_total_tweets(test)
            
        return jsonify(output=test)

# Function to return data on solar in all regoin of melbourne from couchdb views and aurin data


class TweetsOnSolar(Resource):
    def get(self):
        print("Entering database")
        # get the related aurin data
        aurin_result = get_aurin(search_by="topic", search_topic="solar")
        test = []
        regions = []
        labels = []

        # query couchdb view to get the related data
        for db_name in DB_LIST:
            region = ''
            if db_name in ["twitter_north", "twitter_east", "twitter_west", "twitter_south"]:
                region = db_name.split("_")[1]
            else:
                continue

            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey',
                           reduce=True, group=True, group_level=2)

            for item in rows:
                curent_key = item.key
                if(curent_key[0] == 'solar'):
                    label = curent_key[1]
                    result = {}

                    if region not in regions:
                        regions.append(region)
                        result["region"] = region

                    if label == "NEG":
                        labels.append(label)
                        result["NEG"] = item.value
                    elif label == "NEU":
                        labels.append(label)
                        result["NEU"] = item.value
                    elif label == "POS":
                        labels.append(label)
                        result["POS"] = item.value
                    else:
                        continue

                    if 'region' not in result.keys():
                        for i in test:
                            if(i['region'] == region):
                                i[label] = item.value
                                continue
                    else:
                        test.append(result)

            test = compute_total_tweets(test)

        return jsonify(output=test, aurin=aurin_result)
# Function to return data on electric cars in all regoin of melbourne from couchdb views and aurin data


class TweetsOnElectricCars(Resource):
    def get(self):
        print("Entering database")
        # get the related aurin data
        aurin_result = get_aurin(search_by="topic", search_topic="electric_cars")
        test = []
        regions = []
        labels = []

        # query couchdb view to get the related data
        for db_name in DB_LIST:
            region = ''
            if db_name in ["twitter_north", "twitter_east", "twitter_west", "twitter_south"]:
                region = db_name.split("_")[1]
            else:
                continue

            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey',
                           reduce=True, group=True, group_level=2)

            for item in rows:
                curent_key = item.key
                if(curent_key[0] == 'electric_cars'):
                    label = curent_key[1]
                    result = {}

                    if region not in regions:
                        regions.append(region)
                        result["region"] = region

                    if label == "NEG":
                        labels.append(label)
                        result["NEG"] = item.value
                    elif label == "NEU":
                        labels.append(label)
                        result["NEU"] = item.value
                    elif label == "POS":
                        labels.append(label)
                        result["POS"] = item.value
                    else:
                        continue

                    if 'region' not in result.keys():
                        for i in test:
                            if(i['region'] == region):
                                i[label] = item.value
                                continue
                    else:
                        test.append(result)

            test = compute_total_tweets(test)

        return jsonify(output=test, aurin=aurin_result)


api.add_resource(Tweet, '/api/tweet')
api.add_resource(TweetOfNorth, '/api/tweet/north')
api.add_resource(TweetOfSouth, '/api/tweet/south')
api.add_resource(TweetOfWest, '/api/tweet/west')
api.add_resource(TweetOfEast, '/api/tweet/east')
api.add_resource(TweetsOnRecycling, '/api/tweet/recycling')
api.add_resource(TweetsOnSolar, '/api/tweet/solar')
api.add_resource(TweetsOnElectricCars, '/api/tweet/electric_cars')

if __name__ == '__main__':
    couch = couchdb.Server(DB_URI)
    app.run(port='8081', debug=True)
