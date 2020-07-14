""" Driver code for server """

from flask import Flask

from config.loader import CONFIG
from lib import getter, remove, setter
from lib.utils import alerts

app = Flask(__name__)


@app.route('/', methods=['GET'])
def base() -> None:
    """ Handles base requests """
    return 'Key Value Store, powered by Flask!'


@app.route('/get/<string:key>', methods=['GET'])
def get_value(key: str) -> None:
    """ Handles get requests """
    return getter.get_value(key)


@app.route('/set/<string:key>/<string:value>', methods=['GET'])
def set_value(key: str, value: str) -> None:
    """ Handles set requests """
    return setter.set_value(key, value)


@app.route('/remove/<string:key>', methods=['GET'])
def remove_value(key: str) -> None:
    """ Handles delete requests """
    return remove.remove_value(key)


@app.before_first_request
def dummy() -> None:
    """ Dummy function to call send OK alert on successful app startup """
    alerts.pushover('OK', 'Flask server started successfully.')


if __name__ == '__main__':
    try:
        app.run(host=CONFIG['app']['host'], port=CONFIG['app']['port'])
    except Exception as error:
        alerts.pushover('CRITICAL', f'Flask server startup failed. Error: {error}')
