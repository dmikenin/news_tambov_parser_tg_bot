from bs4 import BeautifulSoup
import requests
import time


class ParserOnlineTambov:

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

    def process_data(self, data):
        result_parser = list()
        for item in data:
            result_parser.append('https://www.onlinetambov.ru' + item.attrs["href"])
            # result_parser.append({'title': item.text, 'link': 'https://www.onlinetambov.ru' + item.attrs["href"]})
        return result_parser

    def get_data(self, section):
        total = 0
        while total < 1:
            try:
                req = requests.get('http://www.onlinetambov.ru/news/{}/?PAGEN_4=1'.format(section), timeout=10)
                total += 1
            except requests.exceptions.ConnectionError:
                time.sleep(10)
                total = 0
        soup = BeautifulSoup(req.text, 'lxml')
        result = soup.find_all('a', class_="head")

        return result

    def convert_in_message(self, processed_data):
        message = ''
        for item in processed_data:
            message += '[{title}]({link})'.format(title=item['title'], link=item['link'])
            message += '\n\n'
        return message




    def call(self, section):
        big_data = self.get_data(self.get_name_catalog(section))
        processed_data = self.process_data(big_data)
        # html_data = self.convert_in_message(processed_data)

        return processed_data
        # return html_data