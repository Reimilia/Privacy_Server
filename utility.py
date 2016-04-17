

'''
This file is designed to help make full use of the data in policy in EMR
To convert it from structure_defnition to the normal json layer structure.
'''

'''
{
    "Policy":
    {....
    }
}

Convert to

{
    "Policy":
    [
        {
        "cover": "A":{"B":{"C": "loc"}}}
        "display": Not be seen!
        "Scope": ["A","B"]
        "id": " "
        }
        {
        "cover": "*"
        "display": Not be seen!
        "Scope": ["A","B"]
        "id": " "
        } //This means the whole layer should not been displayed to the user
    ]
}
'''

class Structure_Convertion(object):

    def warp_layer_json(self):
        pass

    def get_patient_id(self):
        pass

    def generate_template_rule(self):
        pass