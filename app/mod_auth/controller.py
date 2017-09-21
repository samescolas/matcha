from flask import Blueprint, render_template, request, url_for, redirect, session, make_response, jsonify
from functools import wraps
import jwt
from .. import User

auth = Blueprint('auth', __name__, template_folder="templates", static_folder="static/auth")

@auth.route('/')
def home():
	if 'loggedin' in session:
		return render_template('home.html');
	#	return redirect(url_for('home'))
	elif 'signedup' not in session:
		return render_template('register.html')
		#return redirect(url_for('auth.register'))
	else:
		return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET'])
def test_login():
	print("inside tets_login");
	return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login():
	print("inside login controller!")
	auth = request.authorization
	print(request)
	if not auth:
		print("no auth")

	if not auth or not auth.username or not auth.password:
		return make_response('Could not verify user.',
				     401,
				     {'WWW-Authenticate' : 'Basic realm="Login Required!"'})

	user = User(auth.username)

	if not user.auth(auth.password):
		return make_response('Could not verify user.',
				     401,
				     {'WWW-Authenticate' : 'Basic realm="Login Required!"'})
	token = jwt.encode({'public_id' : user.data[0], 'exp' : datetime.datetime.now()}, app.config['SECRET_KEY'])
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
