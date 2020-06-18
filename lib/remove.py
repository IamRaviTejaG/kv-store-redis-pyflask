""" Handles removal functionality """

import lib


def remove_value(key: str) -> dict:
    """ Removed entries from redis & database """

    data = dict()
    if key in lib.PROTECTED_KEYS:
        data = {'error': 'Error removing protected keys!'}
    else:
        lib.redisClient.delete(key)
        lib.redisClient.incr('REDIS_CALL_COUNT')  # Increment redis call counter
        lib.redisClient.incr('DATABASE_CALL_COUNT')  # Increment redis db call counter (for deletion)
        db_result = lib.mongoClient.delete_one({'key': key})  # Removes from the database
        if db_result.deleted_count:
            data = {'message': 'Deleted successfully!'}
        else:
            data = {'message': 'No matching entry was found!'}

    return data
