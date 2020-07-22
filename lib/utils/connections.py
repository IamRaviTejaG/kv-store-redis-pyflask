""" Handles connections """

import logging

from pymongo import MongoClient
from redis import Redis

from config.loader import CONFIG
from lib.utils import alerts
from server import logger

logging.basicConfig(level=logging.DEBUG)

try:
    # MongoDB connection
    logger.info('Establishing MongoDB Connection')
    mongo_client = MongoClient(
        f'mongodb+srv://{CONFIG["mongo_atlas"]["username"]}:{CONFIG["mongo_atlas"]["password"]}@{CONFIG["mongo_atlas"]["host"]}/{CONFIG["mongo_atlas"]["db_name"]}',
        CONFIG['mongo_atlas']['port'])
    mongo_client = mongo_client[CONFIG['mongo_atlas']['db_name']]['items']


    # Redis connection
    logger.info('Establishing Redis Connection')

    redis_client = Redis(
        host=CONFIG['redis']['host'],
        port=CONFIG['redis']['port'],
        db=0)


    # Send pushover alert on successful connection.
    alerts.pushover('OK', 'Connection to Redis & MongoDB established successfully.')

except Exception as error:
    alerts.pushover('CRITICAL', f'Error establishing Redis/MongoDB connection. Error: {error}')
