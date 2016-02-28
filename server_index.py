from flask_restful import Resource,Api,abort,reqparse
from flask import Flask
from resources import PrivacyList,Privacy

app = Flask(__name__)
api = Api(app)

api.add_resource(Privacy, '/Privacy')
api.add_resource(PrivacyList, '/Privacy/<patient_id>')

if __name__ == '__main__':
    app.run(port=5000, debug= True)