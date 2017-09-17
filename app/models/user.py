class User:

	def __init__(self, db, email, passwd):
		self.db = db
		print 'inside user with email {} and pass {}'.format(email, passwd)
		self.available = not self.db.get('users', 'email', email)
