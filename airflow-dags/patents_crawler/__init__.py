import datetime
import logging
from typing import List

import csv_exporter
import rest_client
import s3
from model import PatentDto

PAGES_TO_CRAWL = 10
RESULTS_PER_PAGE = 100
logging.basicConfig(level=logging.INFO)


def crawl(keyword: str):
    patents = list()
    crawled_at = _get_date_today_as_str()
    for i in range(1, PAGES_TO_CRAWL + 1):
        logging.info('Crawling patents for keyboard ' + keyword + ". Page " + str(i))
        url = 'https://api.patentsview.org/patents/query'
        query = 'q={"_or":[{"_text_any":{"patent_title":"' + keyword + '"}}]}'
        query_filter = '&f=["patent_id","patent_number","patent_date","patent_title"]&o={"page":' + \
                       str(PAGES_TO_CRAWL) + ',"per_page":' + str(RESULTS_PER_PAGE) + '}'

        request_uri = url + '?' + query + query_filter
        json = rest_client.get(request_uri).json()
        patent_list = _map_response_to_object(json['patents'], keyword)
        for patent in patent_list:
            patents.append(patent)

    logging.info('Finished crawling patents for keyboard ' + keyword)

    tmp_csv = 'patents_' + keyword + '_' + crawled_at + '.csv'
    csv_exporter.export_patterns(tmp_csv, patents)
    s3.upload_to_aws(tmp_csv, '/patents/' + tmp_csv)


def _map_response_to_object(json_list: List[dict], keyword: str) -> List[PatentDto]:
    to_return = list()
    for patent_entry in json_list:
        to_return.append(PatentDto(
            patent_entry['patent_id'],
            patent_entry['patent_number'],
            patent_entry['patent_title'],
            keyword,
            patent_entry['patent_date'],
        ))
    return to_return


def _get_date_today_as_str() -> str:
    dt = datetime.datetime.today()
    return f'{dt.day}-{dt.month}-{dt.year}:{dt.hour}-{dt.minute}-{dt.second}'
