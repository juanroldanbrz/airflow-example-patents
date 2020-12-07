import logging
import time

import requests
from retry import retry


@retry(delay=5, backoff=3, tries=10)
def get(url: str):
    """
    Performs an HTTP GET request and retry if there is an error.
    :param url: URL To GET.
    :return: Returns a HTTP response object.
    """

    time.sleep(1)
    logging.debug(f'Requesting URL {url}')
    response = requests.get(url)
    return response
