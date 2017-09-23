from flask import Blueprint, render_template, request, url_for, redirect, session, make_response, jsonify
from functools import wraps
from .. import User

auth = Blueprint('auth', __name__, template_folder="templates", static_folder="static/auth")

@auth.route('/login', methods=['POST'])
def login():
	auth = request.authorization

	if not auth or not auth.username or not auth.password:
		return make_response('Could not verify user.',
				     401,
				     {'WWW-Authenticate' : 'Basic realm="Login Required!"'})

	user = User(auth.username)
	if not user.auth(auth.password):
		return make_response('Could not verify user.',
				     401,
				     {'WWW-Authenticate' : 'Basic realm="Login Required!"'})
	token = 'test_token'
	return jsonify({'token': token.decode('UTF-8')})

def check_token(token):
        print("Checking token...")
	return token == 'test_token'

def authenticate():
	return redirect(url_for('auth.login'))

def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		if 'token' not in session or not check_token(session['token']):
			return authenticate()
		return f(*args, **kwargs)
	return decorated
