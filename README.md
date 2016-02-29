# Privacy_Server

This little server is developed to solve Privacy_Issue [FHIR-Genomics-2](https://github.com/chaiery/FHIR-Genomics-2)
It should make full usage combined with [this proxy server](https://github.com/Reimilia/Proxy_Server)


## Preparation

```sudo pip install -r requirements.txt```

```sudo apt-get install postgresql```

read [this configuration](./resources/common/db_config.py) to settle your own postgresql database
after check of configuration, run ```python setup_db.py``` to set up database for this server


## How to use

run server_index.py and use curl to test it

For debug purpose, we recommend you to start with
```python server_index.py -d```

The original port is settled at ```http://localhost:5000```, you can change it in [server_index.py](./server_index.py)

Multiple POST:
```curl http://localhost:5000/Privacy -H "Content-Type: application/json" -X POST --data '{"Resource": [{"Identifier":"1", "Policy":[{"a":"b","e":"f"},{"c":"d"}], {"Identifier":"2", "Policy":{"hehe":"haha"}}]}'
```

Single GET:
```curl http://localhost:5000/Privacy/<Patient_id>```

E.g.
```curl http://localhost:5000/Privacy/f01f00a3-a38a-4401-a3e4-53c4239badb4```

Returned json data:
```
{
    "Identifier": "f01f00a3-a38a-4401-a3e4-53c4239badb4", 
    "Resource": {
        "Patient": {
            "gender": "Protected"
        }
    }
}```
**Resource** itself is the policy data we stored in data base


Single PUT:
```curl http://localhost:5000/Privacy/f01f00a3-a38a-4401-a3e4-53c4239badb4 -H "Content-Type: application/json" -X PUT --data '{"UpdatePolicy":{"Patient":{"gender":"Protected"}}}' -v```


Single DELETE:
```curl http://localhost:5000/Privacy/<Patient_id> -X DELETE -v```

