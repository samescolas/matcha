from flask import Blueprint, render_template, request, url_for, redirect, session, make_response, jsonify
from forms import LoginForm, RegistrationForm
from .. import User
import jwt

auth = Blueprint('auth', __name__, template_folder="templates", static_folder="{}/static".format(__file__))

@auth.route('/')
def home():
	if session.get('logged_in'):
		return render_template('index.html');
	#	return redirect(url_for('home'))
	elif request.cookies.get('signedup') == None:
		return redirect(url_for('auth.register'))
	else:
		return redirect(url_for('auth.login'))

@auth.route('/users/', methods=['GET'])
def get_all_users():
	user = User('', '')
	if not user.db.get('users', '1', '1'):
		return jsonify({'message': 'No users found.'}), 404
	users = user.db.results[:]
	obj = {}
	for record in users:
		obj[record[0]] = {
			'user_id': record[0],
			'f_name': record[1],
			'l_name': record[2],
			'age': record[4],
			'gender': record[5],
			'location_id': record[7],
			'sexual_preference': record[10],
			'active': record[11]
		}
	del user
	return jsonify({'data': obj})

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
				resp.set_cookie('signedup', '1')
				return resp
			else:
				return "<h1>Username taken?</h1>"
	return render_template('register.html', form=form)
