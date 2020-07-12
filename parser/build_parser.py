from parser.parser_factory import AbstractFactoryParser


class BuildParserResult:
    def build(self, factory: AbstractFactoryParser, section, user_id):
        result = list()
        result_online_tambov = factory.parsing_online_tambov(section, user_id)

        result += result_online_tambov

        return result

