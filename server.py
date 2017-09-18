from flask import Flask, request, url_for, session, redirect, make_response, g
from flask_wtf.csrf import CSRFProtect
from app import User
from app import auth

app = Flask(__name__)

# CSRF protection
app.secret_key = 's3cret'
csrf = CSRFProtect(app)

# Auth contains all routing from / until logged in.
app.register_blueprint(auth)


#@app.route('/')
#def home():
	#if session.get('logged_in'):
		#return redirect(url_for('home'))
	## This should really be done upon successful registration.
	#elif request.cookies.get('signedup') == None:
		#resp = make_response(redirect(url_for('auth.register')))
		#resp.set_cookie('signedup', '1')
		#return resp
	#else:
		#return redirect(url_for('auth.login'))

#@app.route('/favicon.ico')
#def favicon():
#	return send_from_directory()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
