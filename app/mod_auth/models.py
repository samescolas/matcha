# from app import db

class User():
	name = "Sam"
	email = "samescolas@gmail.com"
	password = "test_pass"
	role = "role?"
	status = "new"

	def __init__(self):
		self.name = name
		self.email = email
		self.password = password

	def __repr__(self):
		return '<User %r>' % (self.name)
