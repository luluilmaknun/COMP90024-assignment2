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