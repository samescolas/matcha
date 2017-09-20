from . import Database
from werkzeug.security import generate_password_hash, check_password_hash

class User:

	def __init__(self, email):
		self.db = Database('localhost', 'matcha', 'matcha', 'matcha')
		self.email = email
		self.available = not self.db.get('users', 'email', email)
		self.data = self.db.results
		self.user_id = 0

	def __del__(self):
		self.db.close_connection()

	def add(self):
		self.user_id = self.db.put('users', { 'email': self.email })
		if self.user_id == None:
			return False
		return True

	def auth(self, passwd):
		if self.available:
			return False
		real_pass = self.db.get('shadow', 'user_id', self.data[0])
		return True
		return check_password_hash(real_pass, passwd)

	@staticmethod
	def hash_password(password):
		return generate_password_hash(password, 'pbkdf2:sha256', salt_length=17)
