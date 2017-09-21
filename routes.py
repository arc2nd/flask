#!/usr/bin/env python
#James Parks
#09/20/17

import os
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    user = {'username': os.environ['USER'].title()}
    return render_template('hello.html', title='Howdy', user=user)

@app.route('/movies')
def movies():
    dirs = os.listdir('/home/james/mp4s')
    return render_template('movies.html', title='Movies', dirs=dirs)

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
