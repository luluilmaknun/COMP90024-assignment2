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


def main(dir, search_region):
    filenames = os.listdir()
    COUCHDB_ADDRESS = "http://dev:dev@172.26.131.7:5984/"
    # Couchdb. Need to have unimelb vpn active
    couchserver = couchdb.Server(COUCHDB_ADDRESS)
    print('\n', couchserver)
    db_name = f"twitter_{search_region}"
    db = create_or_connect_db(couchserver=couchserver,
                            db_name = db_name)
    print(db)

    for filename in filenames:
        if filename.split("_")[0] == search_region:
            with open(f"{dir}/{filename}", "r") as f:
                data = json.load(f)
                for tweets in data['items']:
                    tweets.pop('direction', None)

                    try:
                        tweets_couchified = couchify_tweet(tweets)       
                        print('    uploading on couchdb')
                        db.save(tweets_couchified)
                        print('    upload completed')
                    except couchdb.http.ResourceConflict:
                        pass

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-r", "--region", required=True, type=str, help="type region in lower case")
    args = arg_parser.parse_args()
    search_region = args.region

    main("20220503_1043", search_region)
