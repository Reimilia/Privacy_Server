# Privacy_Server

## Preparation

sudo pip install -r requirements.txt
sudo apt-get install postgresql

then run setup.py
and read /resources/common/db_config.py to settle your own postgresql database


## How to use

run server_index.py and use curl to test it


Multiple POST:
curl http://localhost:5000/Privacy -H "Content-Type: application/json" -X POST --data '{"Resource": [{"Identifier":"1", "Policy":[{"a":"b","e":"f"},{"c":"d"}], {"Identifier":"2", "Policy":{"hehe":"haha"}}]}'

Single GET:
curl http://localhost:5000/Privacy/1

Single PUT:
curl http://localhost:5000/Privacy/2 -H "Content-Type: application/json" -X PUT --data '{"policy":{"zm":"daxuebe"}}'

Single DELETE:
curl http://localhost:5000/Privacy/2 -X DELETE -v
