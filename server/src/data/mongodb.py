import sys
import os
import logging
from pymongo import MongoClient

MONGO_URI = os.environ.get('MARIO_MONGO_URI')
MONGO_DB = os.environ.get('MARIO_MONGO_DB')
MONGO_COLLECTION_GAME = os.environ.get('MARIO_MONGO_COLLECTION_GAME')
MONGO_COLLECTION_PLAYER = os.environ.get('MARIO_MONGO_COLLECTION_PLAYER')

# verify database connection environment variables
if MONGO_URI is None:
	logging.critical("MARIO_MONGO_URI environment variable must be set")
	sys.exit(1)

if MONGO_DB is None:
	logging.critical("MARIO_MONGO_URI environment variable must be set")
	sys.exit(1)

if MONGO_COLLECTION_GAME is None:
	logging.critical("MARIO_MONGO_COLLECTION_GAME environment variable must be set")
	sys.exit(1)

if MONGO_COLLECTION_PLAYER is None:
	logging.critical("MARIO_MONGO_COLLECTION_PLAYER environment variable must be set")
	sys.exit(1)

# connect to the database
client = MongoClient(MONGO_URI)
database = client[MONGO_DB]
player_collection = database[MONGO_COLLECTION_PLAYER]
game_collection = database[MONGO_COLLECTION_GAME]