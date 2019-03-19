import sqlite3

DB_FILE_PATH = 'data/sakila.db'

class Inventory():
	def __init__(self, inventory_id=None, film_id=None, store_id=None, last_update=None):
		self.conn = sqlite3.conn(DB_FILE_PATH)
		self.cursor = self.conn.cursor()
		self.inventory_id = inventory_id
		self.film_id = film_id
		self.store_id = store_id
		self.last_update = last_update

	def search_by_text(self, store_id, text):
		query ='''SELECT inventory.film_id, inventory.inventory_id, inventory.store_id, film.title, film.description
					FROM inventory
					JOIN film 
					on inventory.film_id = film.film_id
					WHERE (inventory.store_id=? OR inventory.store_id=?) AND (film.title LIKE "%?" OR film.description LIKE "%?")'''

		self.film_title = film_title
		self.film_description = film_description




# 1. __init__ - as above, create a new Inventory object, populating it will all data passed in to the function. Use all the parameters you need.
# 2. search_by_text(store_id, text) – 
# this should search for any DVDs in the given store’s inventory 
# which have a title or a description that partially or fully matches the given text. 
# It should return a list of the matching inventory items 
# (which should also include their film information, eg. title, description). 
# If none can be found, it should return an empty list.