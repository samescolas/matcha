from flask import Flask
import MySQLdb

app = Flask(__name__)
db = MySQLdb.connect(host="localhost",
		     user="matcha",
		     passwd="matcha",
		     db="matcha")

@app.route('/')
def hello():
	return 'hello, world!'

@app.route('/<name>')
def hello_name(name):
	return 'hello, {}!'.format(name)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
