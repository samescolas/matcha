import MySQLdb

class Database:

	def __init__(self, my_host, my_user, my_passwd, my_db):

		self.db = MySQLdb.connect(host=my_host,
					  user=my_user,
					  passwd=my_passwd,
					  db=my_db)
		self.curr = self.db.cursor()
		self.error = False
		self.results = []
		self.records = 0

	# Executes query and stores number of records in self.records
	# and results in self.results. Returns True if query returns results.
	def query(self, sql, params=[]):
		self.error = False
		try:
			if len(params) > 0:
				self.records = self.curr.execute(sql, [params])
			else:
				self.records = self.curr.execute(sql)
		except MySQLdb.Error, e:
			print 'MySQL Error: {}'.format(str(e))
			self.error = True
		if not self.error and self.records > 0:
			self.results = self.curr.fetchall()
			return True
		return False
		
	# insert single record into database. Returns id of inserted row.
	def put(self, table, fields):
		sql = "INSERT INTO {} (".format(table)
		params = []
		for key in fields:
			sql += "{}, ".format(key)
		sql = sql[:-2] + ') VALUES ('
		sql = sql + ("%s, " * len(fields))
		sql = sql[:-2] + ');'
		for key in fields:
			params.append(fields[key])
		print(params)
		try:
			self.curr.execute(sql, params)
			self.db.commit()
		except MySQLdb.Error, e:
			print 'MySQL Error: {}'.format(str(e))
			self.error = True
		return self.curr.lastrowid

	# Simple function to get a single record from the database by id or other equivalence.
	def get(self, table, field_id, field_val):
		sql = "SELECT * FROM {} WHERE {} = '{}';".format(table, field_id, field_val)
		return self.query(sql)

	def close_connection(self):
		self.curr.close()
		self.db.close()
