import json
import couchdb

from flask_cors import CORS
from flask import Flask, jsonify
from flask_restful import Resource, Api
from couchdb_config import DB_URI, DB_LIST
from util import *


app = Flask(__name__)
api = Api(app)
CORS(app)


class Analysis(Resource):
    def get(self):
        # Function to return analysis result

        # DUMMY, Change here
        analysis = {}
        analysis["sentiment"] = dummy()

        return jsonify(output=analysis)


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


api.add_resource(Analysis, '/api/analysis')
api.add_resource(Tweet, '/api/tweet')


if __name__ == '__main__':
    couch = couchdb.Server(DB_URI)
    app.run(port='8081',debug=True)
