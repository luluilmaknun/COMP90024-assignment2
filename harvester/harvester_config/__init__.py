AUTH = {
    # lulus
    'west': {
        "CONSUMER_KEY": "mxqyJYQQTjK8GELo7WuyF7PZL",
        "CONSUMER_KEY_SECRET": "GCoiXIGJhixATDaGJPxnRsDAl8wkRFFSGPCQkZdeproCIrfKCV",
        "ACCESS_TOKEN": "1514125532824502275-aGDxWMrxR4Qc1FCip9rxOww7vnGrQu",
        "ACCESS_TOKEN_SECRET": "VY74YrL3o9T48nxM5i4lBKajESQxtX6WYFUlETUYKR2HT"
    },
    # lulus
    'east': {
        "CONSUMER_KEY": "mxqyJYQQTjK8GELo7WuyF7PZL",
        "CONSUMER_KEY_SECRET": "GCoiXIGJhixATDaGJPxnRsDAl8wkRFFSGPCQkZdeproCIrfKCV",
        "ACCESS_TOKEN": "1514125532824502275-aGDxWMrxR4Qc1FCip9rxOww7vnGrQu",
        "ACCESS_TOKEN_SECRET": "VY74YrL3o9T48nxM5i4lBKajESQxtX6WYFUlETUYKR2HT"
    },
    # rislas
    'north': {
        "CONSUMER_KEY": "WpoHCTZpdnBO9GDDb8TaiCPE4",
        "CONSUMER_KEY_SECRET": "stGYLL8cV9VcUSh2wljrkbw9cXQuMoisFQG9e19eH6QfWoIdHe",
        "ACCESS_TOKEN": "1515880143889510400-DRbcnUvKAEBm6JRpSm7rtwbK9ykfJx",
        "ACCESS_TOKEN_SECRET": "UQJk5ZtYk0ncr5Vq8Ko6WCI3pJiobgCts9gWO08sHjc1t"
    },
    # gyus
    'south': {
        "CONSUMER_KEY": "JhsoL6IczdxoEJR1YO9XGdvmD",
        "CONSUMER_KEY_SECRET": "mQBSn7CWZsjgOK71pBb2E2ovhQiaksXMDmRTNhoqsXcLZrSJHd",
        "ACCESS_TOKEN": "1513827450698235907-TOFjLbkVCZpb66kCdJqXLZ6D7jmDVu",
        "ACCESS_TOKEN_SECRET": "bzTSp8Z1TRbwEGQCYS1vvnS0DKXmZMNJNXVrCDMZzuHJ7"
    }
}

KEYWORDS = {
    'electric_cars': [
        "drive electric", "electric future", "electric car", "electric vehicle", "modelx", "ev conversion",
        "elon musk", "tesla ", "tesla life", "tesla car", "tesla roadster", "tesla motors", "tesla model",
        "car charger", "self driving", "urban mobility", "zero emissions", "electric mobility", "emobility",
        "self driving car", "autonomous vehicle", "autonomous car", "future car", "ev sales", "ev battery",
        "autonomous driving", "audietron", "alternative fuel", "connected vehicle", "connected car",
        "mahindra"],
    'recycling': [
        'reuse', 'waste', 'composting', 'landfill', 'conserve', 'receptacles', 'disposal', 'recycle',
        'biodegradable', 'yellow bin', 'e-waste', 'reusable', 'reprocessing', 'recycled', 'recyclebots',
        'waste paper', 'carbon neutral', 'reduce'],
    'solar': [
        'solar', 'solar panels', 'solar battery', 'csp', 'renewable energy', 
        'sun power', 'photovoltaic', 'cell', 'wind turbine', 'hydro', 'solar city', 'windmill',
        'green energy', 'geothermal', 'biomass', 'carbon tax', 'carbon policy', 'C02 footprint', 
        'EBITDA', 'Enova', 'Diamond Energy', 'Momentum Energy', 'Aurora Energy', 'Tilt', 'WestWind',
        'FinnBiogas', 'biogas', 'Acciona'
    ]
}

# LOCATIONS = [144.6845, -38.0815, 145.3540, -37.5934]
LOCATIONS = {}
LOCATIONS["west"] = [144.317, -38.0, 144.856, -37.166]
LOCATIONS["north"] = [144.856, -38.0, 145.185, -37.166]
LOCATIONS["east"] = [145.185, -38.0, 145.901, -37.166]
LOCATIONS["south"] = [144.655, -38.533, 145.901, -38.0]



COUCHDB_ADDRESS = "http://dev:dev@172.26.131.7:5984/"
