from flask import Blueprint, render_template, request, url_for, redirect, session, make_response, jsonify
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

@auth.route('/login/', methods=['GET'])
def test_login():
	return render_template('login.html')

@auth.route('/login/', methods=['POST'])
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

	user = User(auth.email, auth.password)

	if not user.auth(auth.password):
		return make_response('Could not verify user.',
				     401,
				     {'WWW-Authenticate' : 'Basic realm="Login Required!"'})
	token = jwt.encode({'public_id' : user.data[0], 'exp' : datetime.datetime.now()}, app.config['SECRET_KEY'])
	return jsonify({'token': token.decode('UTF-8')})


@auth.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST':
		if form.validate():
			user = User(form.email.data, form.passwd.data)
			if not user.available:
				form.errors['Invalid email'] = 'Email address already exists.'
			if user.add():
				resp = make_response(redirect(url_for('auth.login')))
				session['signedup'] = '1';
				return resp
			else:
				return "<h1>Username taken?</h1>"
	return render_template('register.html', form=form)
