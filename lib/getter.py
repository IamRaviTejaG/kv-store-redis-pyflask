""" Handles getter requests """

import lib


def get_value(key: str) -> dict:
    """ Handles data get requests """

    data = {}

    if key in lib.constants.PROTECTED_KEYS:
        data = {'error': 'Error getting protected keys!'}
    else:
        redis_cache_value = lib.redisUtils.get_and_incr(key, lib.constants.REDIS_CC)
        if redis_cache_value is None:
            lib.redisUtils.incr(lib.constants.DATABASE_CC)
            db_result = lib.mongoClient.find_one({'key': key})
            if db_result is None:
                data = {'error': 'No result found!'}
            else:
                lib.redisUtils.set_and_incr(key, db_result['value'], lib.constants.REDIS_UPDATE_CC)
                data = {key: db_result['value']}
        else:
            lib.redisUtils.expire(key, lib.constants.REDIS_KEY_TTL)
            data = {key: redis_cache_value}

    return lib.jsonify(data)
