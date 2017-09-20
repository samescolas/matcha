from . import Database
from werkzeug.security import generate_password_hash, check_password_hash

class User:

	def __init__(self, email, passwd):
		self.db = Database('localhost', 'matcha', 'matcha', 'matcha')
		self.email = email
		self.passwd = self.hash_password(passwd)
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
	def auth(self):
		self.is_logged_in = True

	@staticmethod
	def hash_password(password):
		return generate_password_hash(password, 'pbkdf2:sha256', salt_length=17)
