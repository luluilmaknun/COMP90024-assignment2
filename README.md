# COMP90024-assignment2

## Development guide
### Backend
Backend is used to fetch data from couchdb. The backend uses `Flask==1.1.4` in `>Python 3.6` with the following dependencies:

```
Flask==1.1.4
Flask-Cors==3.0.10
Flask-RESTful==0.3.9
MarkupSafe==2.0.1
```

**To run:**
1. `cd` into `web/backend`
2. Run command `pip install -r requirements.txt` to install all dependencies
3. Run app with `python app.py`

The app should be running on port `8081`

### Frontend - Map component
**Map component should be run separately from the website!**

**To run:**
1. `cd` into `web/frontend/map-component`
2. Run the command "npm i" to install the dependencies
3. Run the command "npm start" to build and start the application in one go

The component should be running on port `3000` (need to be called by the website)

### Frontend - Website

**To run:**
1. `cd` into `web/frontend`
1. Run the command "npm i" to install the dependencies
2. Run the command "npm run start" to build and start the application in one go

The component should be running on port `4200`
