from app import Database
from app import User

# Example of db.put
stored = db.put('interests', { 'label': 'Coding'})
if stored == None:
	print("Unable to insert data.")
else:
	print("Stored ID: {}".format(stored))

# Example of db.get
result = db.get('interests', 'id', '1')
if result:
	for record in db.results:
		for field in record:
			print(field)

# Example of db.query
another = db.query("SELECT * FROM interests WHERE ID = (%s)", [11])
if another:
	print(db.results)
else:
	print 'No dice.'

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
