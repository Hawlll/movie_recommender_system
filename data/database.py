import sqlite3

#Creates database if doesn't exist already
def databaseInit():
	conn = sqlite3.connect('userdata.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, pwdhash TEXT NOT NULL, preferences TEXT NOT NULL)")
	conn.commit()
	conn.close()
	return 0

#Add a user
def databaseAddUser(name, hash, preferences):
	conn = sqlite3.connect('userdata.db')
	cur = conn.cursor()
	cur.execute("SELECT 1 FROM users WHERE name = ?", (name,))
	names = cur.fetchall()
	if (names != []): return -1
	cur.execute("INSERT INTO users (name, pwdhash, preferences) VALUES (?, ?, ?)", (name, hash, preferences))
	conn.commit()
	conn.close()
	return 0

#Remove a user
def databaseRemoveUser(name):
	conn = sqlite3.connect('userdata.db')
	cur = conn.cursor()
	cur.execute("DELETE FROM users WHERE name = ?", (name,))
	conn.commit()
	conn.close()
	return 0

#Returns a list of all active users
def getUserList():
	conn = sqlite3.connect('userdata.db')
	cur = conn.cursor()
	cur.execute("SELECT name FROM users")
	names = cur.fetchall()
	for i in range(len(names)):
		names[i] = str(names[i][0])
	conn.commit()
	conn.close()
	return names

#Get the preferences of a single user
def getUserPreferences(name):
	conn = sqlite3.connect('userdata.db')
	cur = conn.cursor()
	cur.execute("SELECT preferences FROM users WHERE name = ?", (name,))
	pref = cur.fetchall()
	conn.commit()
	conn.close()
	if (pref == []): return -1
	return str(pref[0][0])

#Authenticate a user
def verifyUser(name, hash):
	conn = sqlite3.connect('userdata.db')
	cur = conn.cursor()
	cur.execute("SELECT 1 FROM users WHERE name = ? AND pwdhash = ?", (name, hash))
	res = cur.fetchall()
	conn.commit()
	conn.close()
	if (res == []): return False
	return True


