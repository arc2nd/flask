#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import sys
import json
import bcrypt
import pymongo
import datetime

##Call Examples
#curl http://localhost:5002/sugar -X POST --data date=09232017 --data time=21.39 --data value=117
#curl http://localhost:5002/chart/08232017-09232017 -X GET

#import requests
#resp = requests.get('http://localhost:5002/sugar', data={'date':'09232017', 'time':21.39, 'value':117})
#resp = requests.get('http://localhost:5002/chart/08232017-09232017')



##make db connection

##make flask app
app = Flask(__name__)
api = Api(app)

##setup parser and accepted arguments
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('user')
parser.add_argument('start_date')
parser.add_argument('end_data')
parser.add_argument('date')
parser.add_argument('time')
parser.add_argument('value')
parser.add_argument('high')
parser.add_argument('low')
parser.add_argument('plaintext')
parser.add_argument('hash')

##info looks like:
##{'date': date, 'variable_name': variable_value}

##Define resources
class SVG(Resource):
    def get(self, date=None):
        start, end = date.split('-')
        print('{} :: {}'.format(start, end))
        ##generate SVG text
        return {'start':start, 'end':end}
    def post(self):
        return 'SVG.post'
    def put(self):
        return 'SVG.put'
    def delete(self):
        return 'SVG.delete'

class BloodSugar(Resource):
    def get(self):
        return 'BloodSugar.get'
    def post(self):
        args = parser.parse_args()
        date = args['date']
        time = args['time']
        value = args['value']
        ##put info into mongodb
        ret_str = 'Sugar\ndate: {}\ntime: {}\nval: {}'.format(date, time, value)
        ret_dict = {'date': date, 'time': time, 'value':value}
        return ret_dict
    def put(self):
        return 'BloodSugar.put'
    def delete(self):
        return 'BloodSugar.delete'

class BloodPressure(Resource):
    def get(self):
        return 'BloodPressure.get'
    def post(self):
        args = parser.parse_args()
        date = args['date']
        high = args['high']
        low = args['low']
        ##put info into mongodb
        ret_str = 'Pressure\ndate: {}\nhigh: {}\nlow: {}'.format(date, high, low)
        return ret_str
    def put(self):
        return 'BloodPressure.put'
    def delete(self):
        return 'BloodPressure.delete'

class Weight(Resource):
    def get(self):
        return 'Weight.get'
    def post(self):
        args = parser.parse_args()
        date = args['date']
        value = args['value']
        ##put info into mondodb
        ret_str = 'Weight\ndate: {}\nval: {}'.format(date, value)
        return ret_str
    def put(self):
        return 'Weight.put'
    def delete(self):
        return 'Weight.delete'

class Crypt(Resource):
    def get(self):
        return 'Crypt.get'
    def post(self):
        args = parser.parse_args()
        plaintext = str(args['plaintext'])
        #print(args['hash'])
        hashed = str(args['hash'])
        #print(hashed)
        if hashed == 'None':
            print('generating salt')
            hashed = bcrypt.gensalt(8)
        try:
            ciphertext = bcrypt.hashpw(plaintext, hashed)
        except:
            #ciphertext = sys.exc_info()
            ciphertext = 'bad salt: {}'.format(sys.exc_info())
        print(ciphertext)
        return ciphertext

class UserHash(Resource):
    def post(self):
        args = parser.parse_args()
        user = str(args['name'])
        print(user)
        client = pymongo.MongoClient()
        all_users = client.website.users
        check_dict = {'name':user}
        records = all_users.find_one(check_dict)
        print(records)
        if records:
            if records.has_key('pw_hash'):
                print(records['pw_hash'])
                return records['pw_hash']
            else:
                return 'error: key'
        else:
            return 'error: records'

##add resources to api
api.add_resource(SVG, '/chart/<date>')
api.add_resource(BloodSugar, '/sugar')
api.add_resource(BloodPressure, '/pressure')
api.add_resource(Weight, '/weight')
api.add_resource(Crypt, '/crypt')
api.add_resource(UserHash, '/hash')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
