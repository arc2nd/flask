#!/usr/bin/env python
#James Parks
#09/20/17

import os
import user
import forms
import datetime
import calendar
from functools import wraps
from flask import Flask, render_template, Response, redirect, url_for, request, session, flash

app = Flask(__name__)
app.config.from_object('config')

root = os.getcwd()

VERBOSITY = 1

def _log(priority, msg):
    if VERBOSITY >= priority:
        print(msg)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        for i in session:
            _log(6, i)
        if 'logged_in' not in session:
            return redirect(url_for('login')) #, next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=["GET", "POST"])
def login():
    form = forms.EmailPasswordForm()
    if form.validate_on_submit():
        new_login = user.User(name=form.email.data)
        _log(1, form.password.data)
        if new_login.verify(passwd=form.password.data):
            ts = calendar.timegm(datetime.datetime.now().timetuple())
            session['user'] = new_login.to_dict()
            session['logged_in'] = ts 
            for i in session:
                _log(6, i)
            return redirect(url_for('index'))
        flash('wrong password')
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    user_name = session['user']['name']
    session.pop('user')
    for i in session:
        _log(6, i)
    return render_template('logout.html', user=user_name)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if not name:
        title = os.environ['USER'].title()
        user = {'username': os.environ['USER'].title()}
    else:
        title = name.title()
        user = {'username': name.title()}
    return render_template('hello.html', title="{}'s Landing Page".format(title), user=user)

@app.route('/movies', methods=['GET'])
@app.route('/movies/<root>', methods=['GET'])
@login_required
def movies(root=''):
    working_dir = os.path.join(os.path.expanduser('~'), root)
    dir_contents = os.listdir(working_dir)
    dir_contents.sort()
    dirs = []
    for e in dir_contents:
        print e
        working_path = os.path.join(working_dir, e)
        if os.path.isdir(working_path):
            dirs.append({'name':e, 'type':'dir', 'path':working_path})
        elif os.path.isfile(os.path.join(working_dir, e)):
            size = str((os.path.getsize(working_path) / 1024) / 1024) 
            dirs.append({'name':e, 'type':'file', 'size':size, 'path':working_path})
        elif os.path.islink(working_path):
            dirs.append({'name':e, 'type':'link'})
    _log(6, dirs)
    return render_template('movies.html', title='Movies', root=root, dirs=dirs)

@app.route('/download', methods=['GET', 'POST'])
@login_required
def download():
    ##take in a url and run youtube-dl on it
    form = forms.UrlForm()
    if form.validate_on_submit():
        cmd = 'youtube-dl {}'.format(form.url.data)
        return redirect(url_for('submit_success'))
    return render_template('download.html', form=form)

@app.route('/convert', methods=['GET', 'POST'])
@login_required
def convert():
    ##take in a url and run convert2audio on it
    form = forms.UrlForm()
    if form.validate_on_submit():
        cmd = 'convert2audio -u {}'.format(form.url.data)
        return redirect(url_for('submit_success'))
    return render_template('convert.html', form=form)

@app.route('/submit_success', methods=['GET'])
def submit_success():
    return render_template('submit_success.html')

@app.route('/a')
@login_required
def a():
    return render_template('a.html', title='A\'s Landing Page')
@app.route('/j')
@login_required
def j():
    return render_template('j.html', title='J\'s Landing Page')
@app.route('/e')
@login_required
def e():
    return render_template('e.html', title='E\'s Landing Page')
@app.route('/f')
@login_required
def f():
    return render_template('f.html', title='F\'s Landing Page')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
