from bs4 import BeautifulSoup
import requests
import time

from parser.parser_factory import AbstractParserOnlineTambov
from services.redis_operation import RedisOperation
import logging


class ParserOnlineTambov(AbstractParserOnlineTambov):
    CATALOG_LINK = {
        'society': 'society',
        'jkh': "jkh",
        'economy': "economy",
        'incident': "incident",
        'culture': "culture",
        'sport': "sport"
    }

    def get_name_catalog(self, section):
        return ParserOnlineTambov.CATALOG_LINK.get(section)

    def process_data(self, data, user_id):
        redis = RedisOperation()
        result_parser = list()
        for item in data:
            link = 'https://www.onlinetambov.ru' + item.attrs["href"]
            if redis.check_link(link, user_id):
                return result_parser
            result_parser.append(link)

        redis.set_link(result_parser[0], user_id)
        return result_parser

    def get_data(self, section):
        total = 0
        while total < 1:
            try:
                req_data = requests.get('http://www.onlinetambov.ru/news/{}/?PAGEN_4=1'.format(section),
                                        timeout=10)
                soup = BeautifulSoup(req_data.text, 'lxml')
                result_data = soup.find_all('a', class_="head")
                total += 1
            except requests.exceptions.ConnectionError:
                time.sleep(10)
                total = 0

        return result_data

    def call(self, section, user_id):
        try:
            big_data = self.get_data(self.get_name_catalog(section))
            processed_data = self.process_data(big_data, user_id)
            return processed_data
        except Exception as e:
            logging.warning('Parser online tambov', e)
            return []