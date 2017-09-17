from app import Database
from app import User

db = Database('localhost', 'matcha', 'matcha', 'matcha')
users = []
usernames = ['samescolas', 'liennecat', '0x11', '000', '000', 'testing', 'something', 'lastone']

for name in usernames:
	users.append(User(db, '{}@gmail.com'.format(name), 'testing'))

for user in users:
	if user.available:
		print 'username {} is available!'.format(user.email)
		if user.create():
			print('user_id {} created!'.format(user.user_id))
		else:
			print('Unable to create user.')
	else:
		print 'username {} is already taken'.format(user.email)
