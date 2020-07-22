""" Handles removal functionality """

from lib import constants
from lib.utils import connections, redis_utils


def remove_value(key: str) -> dict:
    """ Removed entries from redis & database """

    data = {}

    if key in constants.PROTECTED_KEYS:
        data = {'error': 'Error removing protected keys!'}
    else:
        redis_utils.delete_and_incr(key, constants.REDIS_CC)
        redis_utils.incr(constants.DATABASE_CC)
        db_result = connections.mongo_client.delete_one({'key': key})  # Removes from the database
        if db_result.deleted_count:
            data = {'message': 'Deleted successfully!'}
        else:
            data = {'message': 'No matching entry was found!'}

    return data
