""" Consists redis utility functions """

from lib.utils.connections import redis_client
from config import constants


def delete(key: str) -> None:
    """ Deletes key """
    redis_client.delete(key)

def delete_and_incr(key_to_delete: str, key_to_increment: str) -> None:
    """ Deletes a key and increments another key """
    delete(key_to_delete)
    incr(key_to_increment)

def expire(key: str, time: int) -> None:
    """ Sets expiry time for a key """
    redis_client.expire(key, time)

def get_and_incr(key_to_get: str, key_to_increment: str) -> str:
    """ Gets key-value and increments another key """
    incr(key_to_increment)
    return get_key(key_to_get)

def get_key(key: str) -> str:
    """ Gets key """
    value = redis_client.get(key)
    value = value.decode('utf-8') if value is not None else None
    return value

def incr(key: str) -> None:
    """ Increment """
    redis_client.incr(key)

def incr_many(*args: tuple) -> None:
    """ Increments multiple keys """
    [incr(arg) for arg in args]

def set_and_incr(key_to_set: str, value: str, key_to_increment: str) -> None:
    """ Sets key-value and increments another key """
    incr(key_to_increment)
    set_key(key_to_set, value)

def set_key(key: str, value: str) -> None:
    """ Sets key """
    redis_client.set(key, value, ex=constants.REDIS_KEY_TTL)
