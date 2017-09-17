from flask import Flask
from app import Database

app = Flask(__name__)
db = Database('localhost', 'matcha', 'matcha', 'matcha')

@app.route('/')
def hello():
	return 'hello, world!'

@app.route('/<name>')
def hello_name(name):
	return 'hello, {}!'.format(name)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
