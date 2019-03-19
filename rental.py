import sqlite3

DB_FILE_PATH = 'data/sakila.db'

class Rental():
	def __init__(self):
		self.conn = sqlite3.conn(DB_FILE_PATH)
		self.cursor = self.conn.cursor()


# __init__ - as above, create a new Rental object, populating it will all data passed in to the function. Use all the parameters you need.
# 2. return_rental(rental_id) – 
# this should update the return_date field in the rental table for the row 
# which has the given rental_id, to the current date and time. - update set part
# Then, it should update the relevant record in the database. - commit() db part