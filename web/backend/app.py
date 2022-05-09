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

class TweetOfNorth(Resource):
    def get(self):
        # Function to return view from north melbourne from databases
        print("Entering database")
        aurin_result = get_aurin(search_by="region", search_region="north")
        test = []

        db_name ='twitter_north'
        if db_name in DB_LIST:
            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey', reduce=True, group=True, group_level=2)
            for item in rows:
                result = {}
                result["key"] = item.key
                result["value"] = item.value
                test.append(result)

        return jsonify(output=test, aurin=aurin_result)

class TweetOfSouth(Resource):
    def get(self):
        # Function to return view from north melbourne from databases
        print("Entering database")
        aurin_result = get_aurin(search_by="region", search_region="south")
        test = []

        db_name ='twitter_south'
        if db_name in DB_LIST:
            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey', reduce=True, group=True, group_level=2)
            for item in rows:
                result = {}
                result["key"] = item.key
                result["value"] = item.value
                test.append(result)

        return jsonify(output=test, aurin=aurin_result)

class TweetOfWest(Resource):
    def get(self):
        # Function to return view from north melbourne from databases
        print("Entering database")
        aurin_result = get_aurin(search_by="region", search_region="west")
        test = []

        db_name ='twitter_west'
        if db_name in DB_LIST:
            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey', reduce=True, group=True, group_level=2)
            for item in rows:
                result = {}
                result["key"] = item.key
                result["value"] = item.value
                test.append(result)

        return jsonify(output=test, aurin=aurin_result)

class TweetOfEast(Resource):
    def get(self):
        # Function to return view from north melbourne from databases
        print("Entering database")
        aurin_result = get_aurin(search_by="region", search_region="east")
        test = []

        db_name ='twitter_east'
        if db_name in DB_LIST:
            db = couch[db_name]
            rows = db.view('SentimentInfo/SentimentOfKey', reduce=True, group=True, group_level=2)
            for item in rows:
                result = {}
                result["key"] = item.key
                result["value"] = item.value
                test.append(result)

        return jsonify(output=test, aurin=aurin_result)

api.add_resource(Tweet, '/api/tweet')
api.add_resource(TweetOfNorth, '/api/tweet/north')
api.add_resource(TweetOfSouth, '/api/tweet/south')
api.add_resource(TweetOfWest, '/api/tweet/west')
api.add_resource(TweetOfEast, '/api/tweet/east')

if __name__ == '__main__':
    couch = couchdb.Server(DB_URI)
    app.run(port='8081',debug=True)
