from . import Database
from werkzeug.security import generate_password_hash, check_password_hash

class User:

	def __init__(self, email):
		self.db = Database('localhost', 'matcha', 'matcha', 'matcha')
		self.email = email
		self.available = not self.db.get('users', 'email', email)
		self.data = self.db.results[:]
		self.user_id = 0

	def __del__(self):
		if self.db:
			self.db.close_connection()

	def add(self, passwd):
		self.user_id = self.db.put('users', { 'email': self.email })
		if self.user_id == None:
			return False
		success = self.db.put('shadow', {
			'user_id' : self.user_id,
			'passwd' : self.hash_password(passwd)
		}) != None;
		return success

	def get_user_id(self):
		if self.user_id > 0:
			return True
		if len(self.email) < 1:
			return False
		if self.db.get('users', 'email', self.email):
			self.user_id = self.db.results[0][0]
			return True
		else:
			return False

	def auth(self, passwd):
		if self.available:
			return False
		if not self.get_user_id():
			return False
		if self.db.get('shadow', 'user_id', self.user_id):
			print(self.db.results[0][2])
			real_pass = self.db.results[0][2]
		return check_password_hash(real_pass, passwd)

	@staticmethod
	def hash_password(password):
		return generate_password_hash(password, 'pbkdf2:sha256', salt_length=17)
