from flask import Flask, request, url_for
from app import Database
from app import User

app = Flask(__name__)
db = Database('localhost', 'matcha', 'matcha', 'matcha')

# Example of db.put
stored = db.put('interests', { 'label': 'Coding'})
if stored == None:
	print("Unable to insert data.")
else:
	print("Stored ID: {}".format(stored))

# Example of db.get
result = db.get('interests', 'id', '1')
if result:
	for record in db.results:
		for field in record:
			print(field)

# Example of db.query
another = db.query("SELECT * FROM interests WHERE ID = (%s)", [11])
if another:
	print(db.results)
else:
	print 'No dice.'

@app.route('/')
def home():
	if not session.get('logged_in'):
		return "<h1>Register</h1>"
	#elif not cookie.get('visited_before'):
	else:
		return "<h1>Hey, boss.</h1>"

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

@app.route('/<name>/')
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
