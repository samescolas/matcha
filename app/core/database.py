import MySQLdb

class Database:

	def __init__(self, my_host, my_user, my_passwd, my_db):

		self.db = MySQLdb.connect(host=my_host,
					  user=my_user,
					  passwd=my_passwd,
					  db=my_db)
		self.curr = self.db.cursor()

	def get(self, table, field_id, field_val):
		sql = "SELECT * FROM {} WHERE {} == {}".format(table, field_id, field_val)
		print(sql)
