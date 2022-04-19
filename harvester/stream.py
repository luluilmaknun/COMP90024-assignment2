import tweepy as tw
import json

from streamer import StreamListener


# Read configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Connect to API stream
auth = tw.OAuthHandler(config["AUTH"]["CONSUMER_KEY"], 
                           config["AUTH"]["CONSUMER_KEY_SECRET"])
auth.set_access_token(config["AUTH"]["ACCESS_TOKEN"], 
                      config["AUTH"]["ACCESS_TOKEN_SECRET"])
api = tw.API(auth, wait_on_rate_limit=True)

# Stream
mystream_listener = StreamListener(keywords=config["KEYWORDS"])
mystream = tw.Stream(auth=api.auth, listener=mystream_listener)

# Filter twitter
print("Start streaming...")
mystream.filter(languages = ["en"], 
                locations=config["LOCATIONS"])
