from flask import Flask, request, url_for, session, redirect, make_response
from app import Database
from app import User
from app import login, register

app = Flask(__name__)
db = Database('localhost', 'matcha', 'matcha', 'matcha')

app.register_blueprint(register, url_prefix='/register')
app.register_blueprint(login, url_prefix='/login')

@app.route('/')
def home():
	if session.get('logged_in'):
		return redirect(url_for('home'))
	# This should really be done upon successful registration.
	elif request.cookies.get('signedup') == None:
		resp = make_response(redirect(url_for('register')))
		resp.set_cookie('signedup', '1')
		return resp
	else:
		return redirect(url_for('login'))

@app.route('/login/')
def login():
	return '<h1>Login</h1>'

@app.route('/register/', methods=['POST'])
def register():
	print(request)
	if request:
		return request
	else:
		redirect_url(url_for('login'))

@app.route('/user/<name>/')
def hello_name(name):
	print 'name: {}'.format(name)
	user = User(db, name, 'test')
	if user.available:
		return 'Welcome, {}!'.format(name)
	else:
		return 'Username {} already exists.'.format(name)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)

@app.route('/favicon.ico')
def favicon():
	return None
