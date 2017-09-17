import MySQLdb

class Database:

	def __init__(self, my_host, my_user, my_passwd, my_db):

		self.db = MySQLdb.connect(host=my_host,
					  user=my_user,
					  passwd=my_passwd,
					  db=my_db)
		self.curr = self.db.cursor()

	def put(self, table, fields):
		sql = "INSERT INTO {} (".format(table)
		vals = ""
		for key in fields:
			sql += "{}, ".format(key)
		sql = sql[:-2] + ') VALUES (%s);'
		for key in fields:
			vals += "{}, ".format(fields[key])
		vals = vals[:-2]
		print(sql)
		try:
			self.curr.execute(sql, [vals])
		except MySQLdb.Error, e:
			print 'MySQL Error: {}'.format(str(e))
		print "Inserted id: {}".format(self.curr.lastrowid)
		self.db.commit()

	def get(self, table, field_id, field_val):
		sql = "SELECT * FROM {} WHERE {} = {};".format(table, field_id, field_val)
		print(sql)
		try:
			records = self.curr.execute(sql)
			if records > 0:
				return self.curr.fetchall()
		except MySQLdb.Error, e:
			print 'MySQL Error: {}'.format(str(e))
