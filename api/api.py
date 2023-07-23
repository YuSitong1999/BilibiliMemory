"""api
请求B站
"""

import json
import logging
import sys
import time

import requests

user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                  'Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'

default_headers: dict[str, str] = {
    'Connection': 'close',
    'User-Agent': user_agent,
}


def set_default_headers_with_cookie(cookie: str):
    """
    设置默认请求头
    :param cookie: cookie
    :return: None
    """
    global default_headers
    default_headers = {
        'Connection': 'close',
        'User-Agent': user_agent,
        'cookie': cookie,
    }


def request_retry_url_list(url_list: list[str], headers: dict[str, str] = None, retry: int = 3) -> requests.Response:
    """
    按顺序请求url列表，每个失败时重试，返回第一个成功的响应
    :param url_list: url列表
    :param headers: 请求头
    :param retry: 重试次数
    :return: 第一个成功的响应
    """
    exception: BaseException | None = None
    for url in url_list:
        try:
            resp = request_retry(url, headers, retry)
            return resp
        except BaseException as e:
            logging.warning(f'request_retry_backup fail, url: "{url}"')
            exception = e
    if exception is None:
        raise Exception('url_list is empty')
    raise exception


def request_retry(url: str, headers: dict[str, str] = None, retry: int = 3) -> requests.Response:
    """
    请求url，失败时重试
    :param url: url
    :param headers: 请求头
    :param retry: 重试次数
    :return: 响应
    """
    global default_headers
    # 始终设置 User Agent
    if headers is None:
        # 直接使用
        headers = default_headers
    else:
        # 设置不存在的字段
        new_headers = default_headers.copy()
        new_headers.update(headers)
        headers = new_headers
    exception: BaseException | None = None
    while retry > 0:
        try:
            time.sleep(1)
            resp = requests.get(url, headers=headers)
            return resp
        except BaseException as e:
            logging.error('request %s error: %s' % (url, sys.exc_info()[0]))
            exception = e
        retry -= 1
    if exception is None:
        raise Exception('should not be here')
    raise exception


def request_retry_json(url: str, headers: dict = None, retry: int = 3) -> dict:
    """
    请求url获取json，失败时重试，返回json
    :param url: url
    :param headers: 请求头
    :param retry: 重试次数
    :return: json
    """
    return json.loads(request_retry(url, headers, retry).text)


class Response:
    def __init__(self, resp: dict):
        self.code: int = resp['code']
        self.message: str = resp['message']
