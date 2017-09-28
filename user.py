#!/usr/bin/env python

import pymongo
import datetime

class User(object):
    def __init__(self, name=None):
        self.name = name
        self.email = None 
        self.first_name = None
        self.last_name = None
        self.middle_name = None
        self.dob = None
        self.timeout = datetime.timedelta(minutes=20)

    #CRUD ops
    def verify(self, passwd=None):
        #encrypt password and check against database
        #if so fill up all the possible fields from 
        #stored data
        return True

    def enroll(self):
        #add user to user database
        return

    def update(self):
        #update user info to database
        return

    def delete(self):
        #delete user from database
        return

    #user ops
    def get_age(self):
        #calculate age
        return

