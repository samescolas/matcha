#!/usr/bin/python
from flask import Flask, request, url_for, session, redirect, make_response, render_template
#from flask_wtf.csrf import CSRFProtect
from app import User, auth, api

app = Flask(__name__)

# CSRF protection
app.secret_key = 's3cret'
#csrf = CSRFProtect(app)

# Set templates folder
app.template_folder = "./static"

# Auth contains all routing from / until logged in.
app.register_blueprint(auth)

# Register api
app.register_blueprint(api)

#@app.route('/favicon.ico')
#def favicon():
#	return send_from_directory()

@app.route('/<garbagio>')
def trashcan(garbagio):
    return redirect(url_for('home'))

@app.route('/')
def home():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
