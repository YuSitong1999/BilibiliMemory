import json
import logging
import time

import requests


def request(url: str, headers=None):
    tot = 3
    while tot > 0:
        try:
            resp = requests.get(url, headers=headers)
            return json.loads(resp.text)
        except BaseException:
            logging.info('request error retry: %s' % url)
            time.sleep(5 - tot)
        tot -= 1
    raise requests.RequestException
