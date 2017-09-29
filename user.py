#!/usr/bin/env python

import pymongo
import datetime
import requests

class User(object):
    def __init__(self, name=None):
        self.name = name
        self.email = None 
        self.first_name = None
        self.last_name = None
        self.middle_name = None
        self.dob = None
        self.timeout = 20

    #CRUD ops
    def verify(self, passwd=None):
        #encrypt password and check against database
        #if so fill up all the possible fields from 
        #stored data
        expected_passwd = self.get_pw_from_db(self.name) #who you say you are
        crypted_passwd = passwd.strip() #self.encrypt_passwd(passwd) replace this with whatever encryption is being used
        if crypted_passwd == expected_passwd:
            self.load_from_db(self.name)
            return True 
        else:
            return False

    def enroll(self):
        #add user to user database
        return

    def update(self):
        #update user info to database
        return

    def delete(self):
        #delete user from database
        return

    def get_pw_from_db(self, name):
        #talk to the db, and get the stored encrypted password for this user
        if name == 'james@here.com':
            return 'thisisatest'
        else:
            return 'notthatone'

    def load_from_db(self, name):
        #talk to the db, load all the attrs for this name into the current object
        return name

    #rest ops
    def encrypt_passwd(self, plaintext):
        #how are you encrypting passwords? I'm going to make a REST service
        ciphertext = requests.post('http://localhost:5002/crypt', data={'plaintext': plaintext})
        return ciphertext

    #user ops
    def get_age(self):
        #calculate age
        return

    def to_dict(self):
        u_dict = {}
        u_dict['name'] = self.name
        u_dict['email'] = self.email
        u_dict['first_name'] = self.first_name
        u_dict['middle_name'] = self.middle_name
        u_dict['last_name'] = self.last_name
        u_dict['dob'] = self.dob
        u_dict['timeout'] = self.timeout
        return u_dict
        
    def from_dict(self, u_dict):
        self.name = u_dict['name']
        self.email = u_dict['email']
        self.first_name = u_dict['first_name']
        self.middle_name = u_dict['middle_name']
        self.last_name = u_dict['last_name']
        self.dob = u_dict['dob']
        self.timeout = u_dict['timeout']

