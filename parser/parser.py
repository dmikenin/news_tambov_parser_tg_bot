from parser.online_tambov import ParserOnlineTambov


class Parser:
    def __init__(self):
        self._online_tambov = ParserOnlineTambov()

    def call(self, section, user_id):
        result_list = list()
        result_list.extend(self._online_tambov.call(section, user_id))

        return result_list
