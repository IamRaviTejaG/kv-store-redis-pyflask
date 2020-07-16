""" Handles alerting via different channels """

import requests

from config.loader import CONFIG


def pushover(status: str, message: str) -> None:
    """ Sends pushover alerts """
    url = CONFIG['alerts']['pushover_url']
    params = {
        'token': CONFIG['alerts']['pushover_token'],
        'user': CONFIG['alerts']['pushover_user_key'],
        'title': f'STATUS - {status}',
        'message': f'{CONFIG["app"]["ec2_machine_dns_url"]} - {CONFIG["app"]["machine_name"]} - {CONFIG["app"]["app_name"]}: {message}"'}
    resp = requests.post(url, params=params)
    print(f'{resp.status_code} - {resp.text}')
