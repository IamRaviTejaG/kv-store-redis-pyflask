import requests

from lib import CONFIG


def pushover(status: str, message: str) -> None:
    url = CONFIG['alerts']['pushover_url']
    params = {
        'token': CONFIG['alerts']['pushover_token'],
        'user': CONFIG['alerts']['pushover_user_key'],
        'title': f'STATUS - {status}',
        'message': f'{CONFIG["app"]["ec2_machine_dns_url"]} - {CONFIG["app"]["machine_name"]} - {CONFIG["app"]["app_name"]}: {message}"'}
    r = requests.post(url, params=params)
    print(f'{r.status_code} - {r.text}')
