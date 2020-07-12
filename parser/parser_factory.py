from abc import ABC, abstractmethod

from parser.online_tambov import ParserOnlineTambov


class AbstractFactoryParser(ABC):

    @abstractmethod
    def parsing_online_tambov(self, section, user_id):
        pass

    # @abstractmethod
    # def parsing_future_site(self:
    #     pass


class ParserFactory(AbstractFactoryParser):

    def parsing_online_tambov(self, section, user_id):
        parser =  ParserOnlineTambov()
        return parser.call(section, user_id)

    # @abstractmethod
    # def parsing_future_site(self:
    #     pass


class AbstractParserOnlineTambov(ABC):

    @abstractmethod
    def get_name_catalog(self, section):
        pass

    @abstractmethod
    def process_data(self, data, user_id):
        pass

    @abstractmethod
    def get_data(self, section):
        pass

    @abstractmethod
    def call(self, section, user_id):
        pass
