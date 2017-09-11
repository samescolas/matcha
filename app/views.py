from app import app

@app.route('/')
@app.route('/index')
def index():
	return 'Hello, world!'

@app.route('/login')
def login():
	return '<h1>Login</h1>'
