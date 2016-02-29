import requests,json
from server_index import HOST
BASE = 'http://'+HOST+'/Privacy'

example_data={
    "Resource": [{
        "Identifier": "1",
        "resourceType": "Patient",
        "Policy": {
            "gender" : "hide",
            "name" : "whatever"
        }},
        {
        "Identifier": "2",
        "resourceType": "Observation",
        "Policy": {
            "datetime": "secret"
        }}]
    }

single_example_data={
    'UpdatePolicy': {'gender': 'Protected'},
    'Identifier': 'f01f00a3-a38a-4401-a3e4-53c4239badb4',
    'resourceType': 'Patient',
    }

if __name__ == '__main__':
    requests.delete('%s/1')
    requests.delete('%s/2')
    resp = requests.post('%s' %(BASE), data=json.dumps(example_data), headers={'Content-Type': 'application/json'})
    print resp._content
    resp = requests.get('%s/1' %BASE)
    print resp._content
    resp = requests.put('%s/f01f00a3-a38a-4401-a3e4-53c4239badb4' %BASE , data=json.dumps(single_example_data), headers={'Content-Type': 'application/json'})
    print resp._content
    resp = requests.delete('%s/1' %BASE)
    print resp._content
    resp = requests.get('%s/1' %BASE)
    print resp._content