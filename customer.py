import sqlite3

DB_FILE_PATH = 'data/sakila.db'

class Customer():
	def __init__(self, customer_id=None, store_id=None, email=None, first_name=None, last_name=None, address_id=None, create_date=None, last_update=None):
		self.conn = sqlite3.conn(DB_FILE_PATH)
		self.cur = self.conn.cur()
		self.customer_id = customer_id
		self.store_id = store_id
		self.email = email
		self.first_name = first_name
		self.last_name = last_name
		self.address_id = address_id
		self.create_date = create_date
		self.last_update = last_update

	def save(self):
		query = ''' UPDATE customer SET store_id = ?, email = ?, first_name = ?, last_name = ?, address_id = ?, create_date = ?, last_update = ?
				WHERE customer_id = ? '''
		data = (self.store_id, self.email, self.first_name, self.last_name, self.address_id, self.create_date, self.last_update, self.customer_id)
    	self.cur.execute(query, data)
    	self.conn.commit()
    	self.conn.close()

	def search_by_email(self, email):
		query = '''SELECT customer_id, store_id, email, first_name, last_name, address_id, create_date , last_update 
				FROM customer WHERE email LIKE ?'''
		data = (email, )
		self.cur.execute(query, data)
		customer=self.cur.getone()
		if customer != None: 
			customer_object = Customer(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5], customer[6], customer[7])
			return customer_object
		else:
			return None

	def get_all(self):
		query = '''SELECT customer_id, store_id, email, first_name, last_name, address_id, create_date , last_update FROM customer'''
		self.cur.execute(query)
		customers_list = []
		for customer in self.cur.getall():
			single_customer = Customer(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5], customer[6], customer[7])
			customer_list.append(single_customer)
			return customer_list


# 1. __init__(customer_id, email, first_name, last_name, store_id, address_id, create_date, last_update) – create a new Customer object and populate it with the given data, but don’t save it to the database. This will be used to create Customer objects from data fetched from the database, as we will see later on.
# 2. save() - this should update the existing record in the database. The data used to update/insert should be the properties of the current object.
# 3. search_by_email(email) – this should do a case insensitive search for a customer 
# by the given email. If found, it should return the customer as a Customer object. 
# If not, it should return None.
# 4. get_all() - get a list of all customers in the database (as a list of Customer objects).