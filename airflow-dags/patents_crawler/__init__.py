import logging
from datetime import datetime
from typing import List

import requests

import csv_exporter
import s3
from model import PatentDto

PAGES_TO_CRAWL = 10
RESULTS_PER_PAGE = 100
logging.basicConfig(level=logging.INFO)


def crawl(keyword: str):
    """
    Crawl patents based in a keyboard and export the data as CSV in AWS S3.
    :param keyword: Keyword to search for in the patents API.
    """

    patents = list()
    crawled_at = _get_date_today_as_str()
    for i in range(1, PAGES_TO_CRAWL + 1):
        logging.info('Crawling patents for keyboard ' + keyword + ". Page " + str(i))
        url = 'https://api.patentsview.org/patents/query'
        query = 'q={"_or":[{"_text_any":{"patent_title":"' + keyword + '"}}]}'
        query_filter = '&f=["patent_id","patent_number","patent_date","patent_title"]&o={"page":' + \
                       str(PAGES_TO_CRAWL) + ',"per_page":' + str(RESULTS_PER_PAGE) + '}'

        request_uri = url + '?' + query + query_filter
        json = requests.get(request_uri).json()
        patent_list = _map_response_to_object(json['patents'], keyword)
        for patent in patent_list:
            patents.append(patent)

    logging.info('Finished crawling patents for keyboard ' + keyword)

    tmp_csv = 'patents_' + keyword + '_' + crawled_at + '.csv'
    csv_exporter.export_patents(tmp_csv, patents)
    s3.upload_to_aws(tmp_csv, '/patents/' + tmp_csv)


def _map_response_to_object(json_list: List[dict], keyword: str) -> List[PatentDto]:
    to_return = list()
    for patent_entry in json_list:
        to_return.append(PatentDto(
            patent_id=patent_entry['patent_id'],
            patent_nr=patent_entry['patent_number'],
            patent_title=patent_entry['patent_title'],
            keyword=keyword,
            patent_date=patent_entry['patent_date'],
        ))
    return to_return


def _get_date_today_as_str() -> str:
    return datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
