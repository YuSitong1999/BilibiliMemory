import json
import logging
import sys
import time
import requests


def request_retry(url: str, headers: dict = None, retry: int = 3) -> requests.Response:
    if headers is None:
        headers = {'Connection': 'close'}
    headers['Connection'] = 'close'
    while retry > 0:
        try:
            resp = requests.get(url, headers=headers)
            return resp
        except:
            logging.error('request %s error: %s' % (url, sys.exc_info()[0]))
            time.sleep(5 - retry)
        retry -= 1
    raise requests.RequestException


def request_retry_json(url: str, headers=None, retry: int = 3) -> dict:
    return json.loads(request_retry(url, headers, retry).text)
