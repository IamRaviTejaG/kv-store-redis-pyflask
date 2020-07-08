""" Driver code for server """

from flask import Flask
from flask_script import Manager


from config.loader import CONFIG
from lib import getter, remove, setter
from lib.utils import alerts


app = Flask(__name__)
manager = Manager(app)


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


@manager.command
def runserver():
    """ Sends alert on successful server startup. Hooked before the first
    request. """
    try:
        app.run(host=CONFIG['app']['host'], port=CONFIG['app']['port'])
        alerts.pushover('OK', 'Flask server started successfully.')
    except Exception as e:
        alerts.pushover('CRITICAL', f'Flask server failed to start. Error: {e}')
  

if __name__ == '__main__':
    manager.run()
