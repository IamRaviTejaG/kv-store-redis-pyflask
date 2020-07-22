""" Project constants """


DECORATOR = '========================================================'
DATABASE_CC = 'DATABASE_CALL_COUNT'
REDIS_CC = 'REDIS_CALL_COUNT'
REDIS_UPDATE_CC = 'REDIS_UPDATE_CALL_COUNT'

REDIS_KEY_TTL = 21600

PROTECTED_KEYS = (
    DATABASE_CC,
    REDIS_CC,
    REDIS_UPDATE_CC)
