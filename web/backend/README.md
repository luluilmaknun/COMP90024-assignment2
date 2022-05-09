# Backend
The backend uses `Flask==1.1.4` in `>Python 3.6` with the following dependencies:

```
Flask==1.1.4
Flask-Cors==3.0.10
Flask-RESTful==0.3.9
MarkupSafe==2.0.1
```

## Steps to run
1. Run command `pip install -r requirements.txt` to install all dependencies
2. Run app with `python app.py`

The app should be running on port `8081`

## Development
1. `util.py` is meant to store data analysis function which will be used in the API
2. Add the function to `app.py` in the appropriate class methods and adjust the json files
3. Add dependencies to `requirements.txt`

## API Endpoint

`HOST https://127.0.0.1:8081/` (Development on local)

### Get analysis result based on region

#### Request
`GET /api/tweet/{search_region}/`

Available `{search_region}`: 
* `north`
* `south`
* `west`
* `east`

#### Response
Response body (serialized JSON) example:

    {
        "aurin": {
            "description": {
                "avg_dwelings": "Average number of dwelings", 
                "avg_dwelings_with_mv": "Average number of dwelings with at least one motor vehicle", 
                "avg_solar_installation": "Average number of solar installation", 
                "perha_solar_installation": "Ratio number of solar installation per hectare", 
                "ratio_dwelings_with_mv": "Ratio number of dwelings with at least one motor vehicle per total dwelings", 
                "total_dwelings": "Total number of dwelings", 
                "total_dwelings_with_mv": "Total number of dwelings with at least one motor vehicle", 
                "total_solar_installation": "Total number of solar installation"
            }, 
            "result": {
                "east": {
                    "motor_vehicle": {
                        "avg_dwelings": 4145.208333333333, 
                        "avg_dwelings_with_mv": 4028.5208333333335, 
                        "ratio_dwelings_with_mv": 0.9718500276423582, 
                        "total_dwelings": 198970, 
                        "total_dwelings_with_mv": 193369
                    }, 
                    "solar": {
                        "avg_solar_installation": 762.875, 
                        "perha_solar_installation": 0.12271168083301048, 
                        "total_solar_installation": 36618
                    }
                }
            }
        }, 
        "output": [
            {
            "key": [
                "electric_cars", 
                "NEG"
            ], 
            "value": 5
            }, 
            {
            "key": [
                "electric_cars", 
                "NEU"
            ], 
            "value": 3
            }, 
            {
            "key": [
                "electric_cars", 
                "POS"
            ], 
            "value": 1
            }, 
            {
            "key": [
                "recycling", 
                "NEG"
            ], 
            "value": 55
            }, 
            {
            "key": [
                "recycling", 
                "NEU"
            ], 
            "value": 29
            }, 
            {
            "key": [
                "recycling", 
                "POS"
            ], 
            "value": 20
            }, 
            {
            "key": [
                "solar", 
                "NEG"
            ], 
            "value": 30
            }, 
            {
            "key": [
                "solar", 
                "NEU"
            ], 
            "value": 48
            }, 
            {
            "key": [
                "solar", 
                "POS"
            ], 
            "value": 63
            }
        ]
    }

There are two components on the response:
* `aurin`: Result of AURIN data analysis
* `output`: Result of Twitter sentiment analysis from database view in couch DB
