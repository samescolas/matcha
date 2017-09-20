#!/usr/bin/python
from flask import Flask, request, url_for, session, redirect, make_response
#from flask_wtf.csrf import CSRFProtect
from app import User
from app import auth

app = Flask(__name__)

# CSRF protection
app.secret_key = 's3cret'
#csrf = CSRFProtect(app)

# Auth contains all routing from / until logged in.
app.register_blueprint(auth)

#@app.route('/favicon.ico')
#def favicon():
#	return send_from_directory()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
