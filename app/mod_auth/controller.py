from flask import Blueprint, render_template, request, url_for, redirect, session, make_response, jsonify
from forms import LoginForm, RegistrationForm
from .. import User

auth = Blueprint('auth', __name__, template_folder="templates")

@auth.route('/')
def home():
	return render_template('index.html');
	if session.get('logged_in'):
		return redirect(url_for('home'))
	elif request.cookies.get('signedup') == None:
		return redirect(url_for('auth.register'))
	else:
		return redirect(url_for('auth.login'))

@auth.route('/user/', methods=['GET'])
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

@auth.route('/login/', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User(form.email.data, form.passwd.data)
		if not user.available:
			form.errors['Invalid email'] = 'Email address does not exist'
		user.auth()
		if user.is_logged_in:
			return "<h1>Home</h1>"
		else:
			form.errors['Invalid password'] = 'Invalid password'
	return render_template('login.html', form=form)


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
