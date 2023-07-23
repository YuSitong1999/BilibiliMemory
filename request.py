'''
import json
import logging
import sys
import time
import requests

user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'

# FIXME cookie 实测有这一个就行，以后可能有变化
cookie: str = 'bsource=1'

default_headers: dict[str, str] = {
    'Connection': 'close',
    'User-Agent': user_agent,
    'cookie': cookie,
}


def request_retry_url_list(url_list: list[str], headers: dict = None, retry: int = 3) -> requests.Response:
    exception: BaseException
    for url in url_list:
        try:
            resp = request_retry(url, headers, retry)
            return resp
        except BaseException as e:
            logging.warning(f'request_retry_backup fail, url: "{url}"')
            exception = e
    raise exception


def request_retry(url: str, headers: dict = None, retry: int = 3) -> requests.Response:
    # 始终设置 User Agent
    if headers is None:
        headers = default_headers
    else:
        new_headers = default_headers.copy()
        new_headers.update(headers)
        headers = new_headers
    # logging.info(f'headers {headers}')
    exception: BaseException
    while retry > 0:
        try:
            resp = requests.get(url, headers=headers)
            return resp
        except BaseException as e:
            logging.error('request %s error: %s' % (url, sys.exc_info()[0]))
            exception = e
            time.sleep(5 - retry)
        retry -= 1
    raise exception


def request_retry_json(url: str, headers: dict = None, retry: int = 3) -> dict:
    return json.loads(request_retry(url, headers, retry).text)
'''
