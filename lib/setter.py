""" Handles setter requests """

import lib


def set_value(key: str, value: str) -> dict:
    """ Handles data set operations """

    data = {}

    if key in lib.constants.PROTECTED_KEYS:
        data = {'error': 'Error setting protected keys!'}
    else:
        lib.redisUtils.incr(lib.constants.REDIS_CC)
        lib.redisUtils.incr(lib.constants.DATABASE_CC)  # Increment redis db call counter (for write operation below)
        db_result = lib.mongoClient.update_one({'key': key}, {'$set': {'value': value}}, upsert=True)
        if db_result.modified_count:
            lib.redisUtils.set_and_incr(key, value, lib.constants.REDIS_UPDATE_CC)
            data = {'message': 'New value set successfully!'}
        elif db_result.upserted_id:
            lib.redisUtils.set_and_incr(key, value, lib.constants.REDIS_UPDATE_CC)
            data = {'message': 'New value inserted successfully!'}
        else:
            data = {'error': 'Data hasn\'t been modified!'}

    return data
