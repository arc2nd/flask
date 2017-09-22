!#/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api
import json
import pymongo

##make db connection

##make flask app
app = Flask(__name__)
api = Api(app)

##info looks like:
##{'date': date, 'variable_name': variable_value}

##Define resources
class SVG(Resource):
    def get(self, start_date, end_date):
        ##generate SVG text
        return

class BloodSugar(Resource):
    def post(self, date, time, value):
        ##put info into mongodb
        return

class BloodPressure(Resource):
    def post(self, date, high, low):
        ##put info into mongodb
        return

class Weight(Resource):
    def post(self, date, value):
        ##put info into mondodb
        return

##add resources to api
api.add_resource(SVG, '/chart/<info>')
api.add_resource(BloodSugar, '/sugar/<info>')
api.add_resource(BloodPressure, '/pressure/<info>')
api.add_resource(Weight, '/weight/<info>')

if __name__ == '__main__':
    app.run(port='5002')
