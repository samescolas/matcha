from app import Database
from app import User

db = Database('localhost', 'matcha', 'matcha', 'matcha')
users = []
usernames = ['samescolas', 'liennecat', '0x11', '000', '000', 'testing', 'something', 'lastone']

for name in usernames:
	user = User(db, '{}@gmail.com'.format(name), 'testing')
	users.append(user)
	if user.available:
		print 'username {} is available!'.format(user.email)
		if user.create():
			print('user_id {} created!'.format(user.user_id))
		else:
			print('Unable to create user.')
	else: # load user from database
		print 'username {} is already taken'.format(user.email)
