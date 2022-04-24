from pysentimiento.preprocessing import preprocess_tweet


def get_sentiment(sentiment_pipeline, content):
    output = {}
    try: 
        content = preprocess_tweet(content)
        sentiment = sentiment_pipeline(content, truncation=True)
        output = {'id':id, 'tweet': content, 'sentiment': sentiment[0]['label']}

    except: 
        pass
    
    return output
