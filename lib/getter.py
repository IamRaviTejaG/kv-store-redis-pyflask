""" Handles getter requests """

from lib import constants, jsonify
from lib.utils import connections, redis_utils


def get_value(key: str) -> dict:
    """ Handles data get requests """

    data = {}

    if key in constants.PROTECTED_KEYS:
        data = {'error': 'Error getting protected keys!'}
    else:
        redis_cache_value = redis_utils.get_and_incr(key, constants.REDIS_CC)
        if redis_cache_value is None:
            redis_utils.incr(constants.DATABASE_CC)
            db_result = connections.mongo_client.find_one({'key': key})
            if db_result is None:
                data = {'error': 'No result found!'}
            else:
                redis_utils.set_and_incr(key, db_result['value'], constants.REDIS_UPDATE_CC)
                data = {key: db_result['value']}
        else:
            redis_utils.expire(key, constants.REDIS_KEY_TTL)
            data = {key: redis_cache_value}

    return jsonify(data)
