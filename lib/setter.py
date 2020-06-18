""" Handles setter requests """

import lib


def set_value(key: str, value: str) -> dict:
    """ Handles data set operations """

    data = dict()
    if key in lib.PROTECTED_KEYS:
        data = {'error': 'Error setting protected keys!'}
    else:
        lib.redisClient.incr('DATABASE_CALL_COUNT')  # Increment redis db call counter (for write operation below)
        db_result = lib.mongoClient.update_one({'key': key}, {'$set': {'value': value}}, upsert=True)
        if db_result.modified_count:
            lib.redisClient.set(key, value, ex=21600)  # Adds value to redis for update operations
            lib.redisClient.incr('REDIS_UPDATE_TTL_CALL_COUNT')  # Increment redis call counter
            data = {'message': 'New value set successfully!'}
        else:
            data = {'error': 'Data hasn\'t been modified!'}

    return data
