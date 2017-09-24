!#/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json
import pymongo
import datetime

##make db connection

##make flask app
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('start_date')
parser.add_argument('end_data')
parser.add_argument('date')
parser.add_argument('time')
parser.add_argument('value')
parser.add_argument('high')
parser.add_argument('low')

##info looks like:
##{'date': date, 'variable_name': variable_value}

##Define resources
class SVG(Resource):
    def get(self, dates):
        start, end = dates.split('-')
        ##generate SVG text
        return

class BloodSugar(Resource):
    def post(self):
        args = parser.parse_args()
        date = args['date']
        time = args['time']
        value = args['value']
        ##put info into mongodb
        ret_str = 'Sugar\ndate: {}\ntime: {}\nval: {}'.format(date, time, value)
        return ret_str

class BloodPressure(Resource):
    def post(self):
        date = args['date']
        high = args['high']
        low = args['low']
        ##put info into mongodb
        ret_str = 'Pressure\ndate: {}\nhigh: {}\nlow: {}'.format(date, high, low)
        return ret_str

class Weight(Resource):
    def post(self):
        date = args['date']
        value = args['value']
        ##put info into mondodb
        ret_str = 'Weight\ndate: {}\nval: {}'.format(date, value)
        return ret_str

##add resources to api
api.add_resource(SVG, '/chart/<date>')
api.add_resource(BloodSugar, '/sugar')
api.add_resource(BloodPressure, '/pressure')
api.add_resource(Weight, '/weight')

if __name__ == '__main__':
    app.run(port='5002')
