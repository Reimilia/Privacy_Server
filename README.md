# Privacy_Server

## Preparation

```sudo pip install -r requirements.txt```

```sudo apt-get install postgresql```

then ```python setup.py```
and read ```./resources/common/db_config.py``` to settle your own postgresql database


## How to use

run server_index.py and use curl to test it


Multiple POST:
'''curl http://localhost:5000/Privacy -H "Content-Type: application/json" -X POST --data '{"Resource": [{"Identifier":"1", "Policy":[{"a":"b","e":"f"},{"c":"d"}], {"Identifier":"2", "Policy":{"hehe":"haha"}}]}'

Single GET:
curl http://localhost:5000/Privacy/<Patient_id>

E.g.
curl http://localhost:5000/Privacy/f01f00a3-a38a-4401-a3e4-53c4239badb4

Returned json data:

{
    "Identifier": "f01f00a3-a38a-4401-a3e4-53c4239badb4", 
    "Resource": {
        "Patient": {
            "gender": "Protected"
        }
    }
}
The Resource itself is a privacy_list


Single PUT:
curl http://localhost:5000/Privacy/f01f00a3-a38a-4401-a3e4-53c4239badb4 -H "Content-Type: application/json" -X PUT --data '{"UpdatePolicy":{"Patient":{"gender":"Protected"}}}' -v


Single DELETE:
curl http://localhost:5000/Privacy/<Patient_id> -X DELETE -v
