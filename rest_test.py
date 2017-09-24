#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask import make_response

##Call Examples
#curl http://localhost:5002/lo -X POST --data name=James --data msg=fingerberries
#curl http://localhost:5002/lo -X GET
#curl http://localhost:5002/dude/James

##make flask app
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('msg')

##Define resources
class hello(Resource):
    def get(self):
        return 'Hello Rest'
    def post(self, msg='test'):
        args = parser.parse_args()
        retstr = 'Howdy {}\nI\'m a msg: {}'.format(args['name'], args['msg'])
        return retstr

class dude(Resource):
    def get(self, name='Dude'):
        return 'Hello {}'.format(name)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

##add resources to api
api.add_resource(hello, '/lo')
#api.add_resource(hello, '/lo/<msg>')
api.add_resource(dude, '/dude/<name>')

if __name__ == '__main__':
    app.run(port=5002)

