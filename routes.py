#!/usr/bin/env python
#James Parks
#09/20/17

import os
from flask import Flask, render_template, Response, redirect, url_for

app = Flask(__name__)

root = os.getcwd()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        ##check psswd and log in
        return redirect(url_for('/index'))
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if not name:
        user = {'username': os.environ['USER'].title()}
    else:
        user = {'username': name.title()}
    return render_template('hello.html', title="{}'s Landing Page".format(name.title()), user=user

@app.route('/movies/<root>')
def movies(root):
    dir_contents = os.listdir(root)
    dirs = {}
    for e in dir_contents:
        if os.path.isdir(os.path.join(root, e)):
            dirs[e] = 'dir'
        elif os.path.isfile(os.path.join(root, e)):
            size = 5
            dirs[e] = size
        elif os.path.islink(os.path.join(root, e)):
            dirs[e] = 'link'
    return render_template('movies.html', title='Movies', root=root, dirs=dirs)

@app.route('/a')
def a():
    return render_template('a.html', title='A\'s Landing Page')
@app.route('/j')
def j():
    return render_template('j.html', title='J\'s Landing Page')
@app.route('/e')
def e():
    return render_template('e.html', title='E\'s Landing Page')
@app.route('/f')
def f():
    return render_template('f.html', title='F\'s Landing Page')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
