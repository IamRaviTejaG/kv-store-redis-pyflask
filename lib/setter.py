""" Handles setter requests """

from lib import constants
from lib.utils import connections, redis_utils


def set_value(key: str, value: str) -> dict:
    """ Handles data set operations """

    data = {}

    if key in constants.PROTECTED_KEYS:
        data = {'error': 'Error setting protected keys!'}
    else:
        redis_utils.incr(constants.DATABASE_CC)  # Increment redis db call counter (for write operation below)
        db_result = connections.mongo_client.update_one({'key': key}, {'$set': {'value': value}}, upsert=True)
        if db_result.modified_count:
            redis_utils.set_and_incr(key, value, constants.REDIS_UPDATE_CC)
            data = {'message': 'Updated value for pre-existing key successfully!'}
        elif db_result.upserted_id:
            redis_utils.set_and_incr(key, value, constants.REDIS_UPDATE_CC)
            data = {'message': 'New value inserted successfully!'}
        else:
            data = {'error': 'Data hasn\'t been modified!'}

    return data
