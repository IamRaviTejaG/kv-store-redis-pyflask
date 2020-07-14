""" Handles getter requests """

import lib


def get_value(key: str) -> dict:
    """ Handles data get requests """

    data = {}

    if key in lib.PROTECTED_KEYS:
        data = {'error': 'Error getting protected keys!'}
    else:
        lib.redisClient.incr('REDIS_CALL_COUNT')
        redis_cache_value = lib.redisClient.get(key)
        if redis_cache_value is None:
            lib.redisClient.incr('DATABASE_CALL_COUNT')
            db_result = lib.mongoClient.find_one({'key': key})
            if db_result is None:
                data = {'error': 'No result found!'}
            else:
                lib.redisClient.set(key, db_result['value'], ex=21600)  # Set cache in redis for 6 hours
                lib.redisClient.incr('REDIS_UPDATE_TTL_CALL_COUNT')  # Update Redis Update TTL calls counter
                data = {key: db_result['value']}
        else:
            redis_cache_value = redis_cache_value.decode('utf-8')
            lib.redisClient.set(key, redis_cache_value, ex=21600)  # Set cache in redis for 6 hours
            lib.redisClient.incr('REDIS_UPDATE_TTL_CALL_COUNT')  # Update Redis Update TTL calls counter
            data = {key: redis_cache_value}

    return lib.jsonify(data)
