#!/usr/bin/env python

##To run:
## $ export FLASK_APP=hello_world.py
## $ flask run
##     or
## $ export FLASK_APP=hello_world.py
## $ python -m flask run
##     or
## flask run --host=0.0.0.0 ##makes visible from other machines

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello_world')
def hello_world():
    return 'Hello, World'

@app.route('/user/<username>')
def hi_user(username):
    return "Hello, {0}".format(username)

from flask import url_for
with app.test_request_context():
    print url_for('index')
    print url_for('hello_world')
    print url_for('hi_user', username='James')

from flask import request
def do_the_login():
    return "You've logged in"
def show_the_login_form():
    return "You login here"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST';
        do_the_login()
    else:
        show_the_login_form()

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

## Example template
"""
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
"""

from flask import Markup
Markup('<strong>Hello {0}!</strong'.format('<blink>Hacker</blink>'))

from flask import request
with app.test_request_context('/hello', method='POST'):
    assert request.path == 'hello'
    assert request.method == 'POST'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

## can also use
    searchword = request.args.get('key', '')

from flask import request
from werkzeug.utils import secure_filename
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))

## generate key
import os
os.urandom(24)


## more uploading
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''




























