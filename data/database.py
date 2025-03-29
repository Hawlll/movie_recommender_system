import sqlite3

#Creates database if doesn't exist already
def databaseInit():
	conn = sqlite3.connect('userdata.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, pwdhash TEXT NOT NULL, preferences TEXT NOT NULL)")
	conn.commit()
	conn.close()

def databaseAddUser(name, hash, preferences):
	conn = sqlite3.connect('userdata.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO users (name, pwdhash, preferences) VALUES ('{}', '{}', '{}')".format(name, hash, preferences))
	conn.commit()
	conn.close()


