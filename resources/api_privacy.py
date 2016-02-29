from flask_restful import Resource,fields,marshal_with,reqparse
from common.database import not_existed,ok,add_policy,insert_record,delete_record,search_record,select_policy
from errors import PrivacyServerError
from datetime import datetime
from common.json_parser import list2json

'''
    The restful API was designed with the help of flask-restful
    It can deal with certain basic API functions like GET , POST, PUT, DELETE
    TO DO: Authentication Process and Visualization
'''


class Privacy(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('Resource', type= dict, required = True, action = 'append',
                                   help= 'Must provide some resources')
        self.deal_error= PrivacyServerError()

    def get(self):
        '''
        multiple get is not tolerate in this demo!
        :return:
        '''
        self.deal_error.abort_with_unaccessable_error()

    def post(self):
        '''
        multiple post for a list ot privacy_resource
        :return:
        '''
        args = self.reqparse.parse_args()

        if len(args['Resource']) > 0 :
            for key in args['Resource']:
                if 'Identifier' in key and 'Policy' in key:
                    insert_record(key['Identifier'],key['Policy'],datetime.now())
                else:
                    self.deal_error.abort_with_POST_error()
        return "Ok", 200

class PrivacyList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('UpdatePolicy', type= dict, help = 'Must provide update info.')
        self.reqparse.add_argument('Policy', type= dict, help= 'Must provide some Policy if post new one')
        self.deal_error= PrivacyServerError()


    def get(self,patient_id):
        '''
        single read/search, not available with partial search now
        :param privacy_id:
        :return:
        '''
        #args = self.reqparse.parse_args()
        search_result = select_policy(patient_id)
        if search_result == not_existed:
            self.deal_error.abort_with_search_error(patient_id)
        #$print search_result
        return {'Identifier' : patient_id, 'Resource': search_result}

    def post(self,patient_id):
        '''
        Single post
        :param patient_id:
        :return:
        '''
        args = self.reqparse.parse_args()
        if args['Policy'] is None:
            self.deal_error.abort_with_POST_error()
        if search_record(patient_id) == not_existed:
            insert_record(patient_id,args['Policy'],datetime.now())
        else:
            return "You should use PUT method to update a policy", 200
        return select_policy(args['identifer']), 200

    def put(self,patient_id):
        '''
        Single put, it will modify the privacy_policy
        Simply, the Identifier is the same with patient_id and this put method might directly merge these data.
        The best way is to first DELETE then PUT if you want to create a new policy
        :param patient_id:
        :return:
        '''
        args = self.reqparse.parse_args()
        if args['UpdatePolicy'] is None:
            self.deal_error.abort_with_POST_error()
        if search_record(patient_id) == not_existed:
            insert_record(patient_id,args['UpdatePolicy'],datetime.now())
        else:
            add_policy(patient_id,args['UpdatePolicy'],datetime.now())
        return select_policy(patient_id), 200


    def delete(self,patient_id):
        if search_record(patient_id) == ok:
            delete_record(patient_id)
        return 'Successfully deleted {}'.format(patient_id), 200
