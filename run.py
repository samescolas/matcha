from flask import Flask
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
def hello():
	return 'hello, world!'

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
