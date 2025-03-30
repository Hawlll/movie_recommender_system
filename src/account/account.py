import bcrypt
import sys
from pathlib import Path

curDir = Path(__file__).resolve()
curDir = curDir.parent.parent.parent
curDir = curDir / 'data'
sys.path.insert(0, str(curDir))

import database

#Creates a database if one does not exist, primarily an abstraction from the database library
def initializeDatabase():
	database.databaseInit()
	return 0

#Create a user from the front-end data
def createUser(username, password, preferences):
	salt = bcrypt.gensalt()
	prefStr = ''
	if preferences == None:
		prefStr = 'EMPTY'
	elif len(preferences) == 7:
		for i in range(6):
			if preferences[i] == 1:
				prefStr = prefStr + 'T'
			elif preferences[i] == 0:
				prefStr = prefStr + 'F'
			else:
				return -1
		if 0 <= preferences[6] <= 10:
			prefStr = prefStr + 'ABCDEFGHIJK'[preferences[6]]
		else:
			return -1
	return database.databaseAddUser(username, bcrypt.hashpw(password.encode('utf-8'), salt), prefStr)

#Returns True if username and password match to an existing database entry
def verifyUserLogin(username, password):
	if not (username in database.getUserList()): return False
	return bcrypt.checkpw(password.encode('utf-8'), database.getUserHash(username))

#Returns true if user exists
def doesUserExist(username):
	return username in database.getUserList()

#Returns the preference vector of a given user
def getUserVector(username):
	if not doesUserExist(username): return -1
	pref = database.getUserPreferences(username)
	if (pref == 'EMPTY'): return -1
	vec = [0, 0, 0, 0, 0, 0, 0]
	for i in range(6):
		if pref[i] == 'T':
			vec[i] = 1
		elif pref[i] == 'F':
			vec[i] = 0
		else:
			return -1
	if not pref[6] in 'ABCDEFGHIJK': return -1
	vec[6] = 'ABCDEFGHIJK'.index(pref[6])
	return vec

#updates the preferences of a given user
def setUserPreferences(user, pref):
	if not doesUserExist(user): return -1
	prefStr = ''
	if pref == None:
		prefStr = 'EMPTY'
	elif len(preferences) == 7:
		for i in range(6):
			if preferences[i] == 1:
				prefStr = prefStr + 'T'
			elif preferences[i] == 0:
				prefStr = prefStr + 'F'
			else:
				return -1
		if 0 <= preferences[6] <= 10:
			prefStr = prefStr + 'ABCDEFGHIJK'[preferences[6]]
		else:
			return -1
	return database.updateUserPreferences(user, prefStr)

