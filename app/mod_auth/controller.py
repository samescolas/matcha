from flask import Blueprint, render_template, request, url_for, redirect, session, make_response
from forms import LoginForm
from .. import User

auth = Blueprint('auth', __name__, template_folder="templates")

@auth.route('/')
def home():
	if session.get('logged_in'):
		return redirect(url_for('home'))
	# This should really be done upon successful registration.
	elif request.cookies.get('signedup') == None:
		return redirect(url_for('auth.register'))
		#resp = make_response(redirect(url_for('auth.register')))
		#resp.set_cookie('signedup', '1')
		return resp
	else:
		return redirect(url_for('auth.login'))

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


@auth.route('/register/')
def register():
	return render_template('register.html')
