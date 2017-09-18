from flask import Flask, request, url_for, session, redirect, make_response, g
from flask_wtf.csrf import CSRFProtect
from app import User
from app import login, register

app = Flask(__name__)
app.secret_key = 's3cret'
csrf = CSRFProtect(app)

app.register_blueprint(register, url_prefix='/register')
app.register_blueprint(login, url_prefix='/login')

@app.route('/')
def home():
	if session.get('logged_in'):
		return redirect(url_for('home'))
	# This should really be done upon successful registration.
	elif request.cookies.get('signedup') == None:
		resp = make_response(redirect(url_for('register.register_page')))
		resp.set_cookie('signedup', '1')
		return resp
	else:
		return redirect(url_for('login.login_page'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
