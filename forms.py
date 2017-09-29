#!/usr/bin/env python
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, URL

from wtforms.ext.csrf.session import SessionSecureForm
import datetime

class MyBaseForm(SessionSecureForm):
    SECRET_KEY = 'thisisatest'
    TIME_LIMIT = datetime.timedelta(minutes=20)

class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me', validators=[])

class UrlForm(Form):
    url = StringField('URL', validators=[DataRequired(), URL()])
