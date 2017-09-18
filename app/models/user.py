from .. import Database

class User:

	def __init__(self, email, passwd):
		self.db = Database('localhost', 'matcha', 'matcha', 'matcha')
		self.email = email
		self.passwd = passwd
		self.available = not self.db.get('users', 'email', email)
		self.user_id = 0

	def add(self):
		self.user_id = self.db.put('users', { 'email': self.email })
		if self.user_id == None:
			return False
		return True
	def auth(self):
		self.is_logged_in = False
			
