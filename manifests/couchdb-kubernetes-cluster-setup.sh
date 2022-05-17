#!/bin/sh

curl -X POST -H "Content-Type: application/json" http://admin:admin@127.0.0.1:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"admin", "port": 5984, "node_count": "3", "remote_node": "couchdb-1.couch-service>", "remote_current_user": "admin", "remote_current_password": "admin" }'

curl -X POST -H "Content-Type: application/json" http://admin:admin@127.0.0.1:5984/_cluster_setup -d '{"action": "add_node", "host":"couchdb-1.couch-service", "port": 5984, "username": "admin", "password":"admin"}'

curl -X POST -H "Content-Type: application/json" http://admin:admin@127.0.0.1:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"admin", "port": 5984, "node_count": "3", "remote_node": "couchdb-2.couch-service>", "remote_current_user": "admin", "remote_current_password": "admin" }'

curl -X POST -H "Content-Type: application/json" http://admin:admin@127.0.0.1:5984/_cluster_setup -d '{"action": "add_node", "host":"couchdb-2.couch-service", "port": 5984, "username": "admin", "password":"admin"}'

curl -s -X PUT http://admin:admin@localhost:5984/_node/couchdb@$NODENAME/_config/admins/dev -d '"dev"'

curl -X PUT http://dev:dev@127.0.0.1:5984/twitter

curl -X PUT http://dev:dev@127.0.0.1:5984/twitter_hist

curl -X PUT http://dev:dev@127.0.0.1:5984/twitter_east

curl -X PUT http://dev:dev@127.0.0.1:5984/twitter_west

curl -X PUT http://dev:dev@127.0.0.1:5984/twitter_south

curl -X PUT http://dev:dev@127.0.0.1:5984/twitter_north

curl -H 'Content-Type: application/json' -X POST http://dev:dev@localhost:5984/_replicate -d ' {"source": "http://admin:admin@172.26.131.7:5984/twitter", "target": "http://dev:dev@localhost:5984/twitter", "continuous": true} '

curl -H 'Content-Type: application/json' -X POST http://dev:dev@localhost:5984/_replicate -d ' {"source": "http://admin:admin@172.26.131.7:5984/twitter_hist", "target": "http://dev:dev@localhost:5984/twitter", "continuous": true} '

curl -H 'Content-Type: application/json' -X POST http://dev:dev@localhost:5984/_replicate -d ' {"source": "http://admin:admin@172.26.131.7:5984/twitter_east", "target": "http://dev:dev@localhost:5984/twitter_east", "continuous": true} '

curl -H 'Content-Type: application/json' -X POST http://dev:dev@localhost:5984/_replicate -d ' {"source": "http://admin:admin@172.26.131.7:5984/twitter_west", "target": "http://dev:dev@localhost:5984/twitter_west", "continuous": true} '

curl -H 'Content-Type: application/json' -X POST http://dev:dev@localhost:5984/_replicate -d ' {"source": "http://admin:admin@172.26.131.7:5984/twitter_north", "target": "http://dev:dev@localhost:5984/twitter_north", "continuous": true} '

curl -H 'Content-Type: application/json' -X POST http://dev:dev@localhost:5984/_replicate -d ' {"source": "http://admin:admin@172.26.131.7:5984/twitter_south", "target": "http://dev:dev@localhost:5984/twitter_south", "continuous": true} '





