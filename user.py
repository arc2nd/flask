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
        expected_hashed = self.get_pw_from_db(self.name) #who you say you are
        hashed_passwd = self.encrypt_passwd(passwd, expected_hashed) #replace this with whatever hashing is being used
        if hashed_passwd != 'error' and hashed_passwd == expected_hashed:
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
    def encrypt_passwd(self, plaintext, hashed=None):
        #how are you hashing passwords? I'm using a REST service
        resp = requests.post('http://localhost:5002/crypt', data={'plaintext': plaintext, 'hash':hashed})
        ##process response for extraneous characters
        if resp.ok:
            ciphertext = resp.text
            if ciphertext.endswith('\n'):
                ciphertext = ciphertext[:-2]
            if ciphertext.startswith('"'):
                ciphertext = ciphertext[1:]
            if ciphertext.endswith('"'):
                ciphertext = ciphertext[:-1]
        else:
            ciphertext = 'error'
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

