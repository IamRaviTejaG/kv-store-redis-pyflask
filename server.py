""" Driver code for server """

from flask import Flask

from config.loader import CONFIG
from lib import getter, remove, setter


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


if __name__ == '__main__':
    app.run(host=CONFIG['app']['host'], port=CONFIG['app']['port'])
