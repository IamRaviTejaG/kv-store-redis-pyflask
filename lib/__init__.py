""" Contains all the common imports """

import logging

from flask import jsonify
from pymongo import MongoClient
from redis import Redis

from config.constants import PROTECTED_KEYS
from config.loader import CONFIG
from server import app

logging.basicConfig(level=logging.DEBUG)


# MongoDB connection
app.logger.info('Establishing MongoDB Connection')
mongoClient = MongoClient(
    f'mongodb+srv://{CONFIG["mongo_atlas"]["username"]}:{CONFIG["mongo_atlas"]["password"]}@{CONFIG["mongo_atlas"]["host"]}/{CONFIG["mongo_atlas"]["db_name"]}',
    CONFIG['mongo_atlas']['port'])
mongoClient = mongoClient[CONFIG['mongo_atlas']['db_name']]['items']


# Redis connection
app.logger.info('Establishing Redis Connection')
redisClient = Redis(
    host=CONFIG['redis']['host'],
    port=CONFIG['redis']['port'],
    db=0)
