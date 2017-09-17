class User:

	def __init__(self, db, email, passwd):
		self.db = db
		self.email = email
		self.passwd = passwd
		self.available = not self.db.get('users', 'email', email)
		self.user_id = 0

	def create(self):
		self.user_id = self.db.put('users', { 'email': self.email })
		if self.user_id == None:
			return False
		return True
			
