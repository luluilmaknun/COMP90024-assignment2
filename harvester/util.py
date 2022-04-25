from pysentimiento.preprocessing import preprocess_tweet
from decimal import Decimal
import json

# can't have 'Decimal' type in JSON it seems
class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

# def get_sentiment(sentiment_pipeline, content):
#     output = {}
#     try: 
#         content = preprocess_tweet(content)
#         sentiment = sentiment_pipeline(content, truncation=True)
#         output = {'id':id, 'tweet': content, 'sentiment': sentiment[0]['label']}

#     except: 
#         pass
    
#     return output


# run sentiment analysis on text data
def get_sentiment(sentiment_analyzer, tweet_text):
    content = preprocess_tweet(tweet_text)
    try:
        sentiment = sentiment_analyzer.predict(content)
    except:
        pass
    # return sentiment label (POS/NEU/NEG) and probability (softmax output)
    return sentiment.__dict__['output'], max(sentiment.__dict__['probas'].values())
       
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
