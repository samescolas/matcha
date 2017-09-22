from flask import Blueprint, render_template, request, url_for, redirect, session, make_response, jsonify
from functools import wraps
from .. import User

auth = Blueprint('auth', __name__, template_folder="templates", static_folder="static/auth")

@auth.route('/login', methods=['GET'])
def test_login():
	print("inside tets_login");
	return render_template('login.html')

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

def check_auth(username, password):
	"""This function is called to check if a user/pass is valid."""
	return ''

def authenticate():
		"""Sends user back to the login page."""
		return ''

def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			return authenticate()
		return f(*args, **kwargs)
	return decorated
