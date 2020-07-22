""" Handles removal functionality """

import lib


def remove_value(key: str) -> dict:
    """ Removed entries from redis & database """

    data = {}

    if key in lib.constants.PROTECTED_KEYS:
        data = {'error': 'Error removing protected keys!'}
    else:
        lib.redisUtils.delete_and_incr(key, lib.constants.REDIS_CC)
        lib.redisUtils.incr(lib.constants.DATABASE_CC)
        db_result = lib.mongoClient.delete_one({'key': key})  # Removes from the database
        if db_result.deleted_count:
            data = {'message': 'Deleted successfully!'}
        else:
            data = {'message': 'No matching entry was found!'}

    return data
