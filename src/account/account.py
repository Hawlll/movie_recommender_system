import bcrypt
import sys
from pathlib import Path

curDir = Path(__file__).resolve()
curDir = curDir.parent.parent.parent
curDir = curDir / 'data'
sys.path.insert(0, str(curDir))

import database

def createUser(username, password, preferences):
	salt = bcrypt.gensalt()
	return database.databaseAddUser(username, bcrypt.hashpw(password.encode('utf-8'), salt), preferences)

def verifyUserLogin(username, password):
	if not (username in database.getUserList()): return False
	return bcrypt.checkpw(password.encode('utf-8'), database.getUserHash(username))

def doesUserExist(username):
	return username in database.getUserList()


