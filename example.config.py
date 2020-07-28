TOKEN = 'XXXXXX:XXXXXXXXX'

# webhook settings
WEBHOOK_HOST = 'https://00.111.2222.333'
WEBHOOK_PATH = '/path/to/api'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001

#section
section_dict= {
    'society':'Общество',
    'jkh': "ЖКХ",
    'economy': "Экономика",
    'incident':"Проишествия",
    'culture':"Культура",
    'sport':"Спорт"
}

#get section keys for keyboard
keys_section_list = list()
for item in section_dict.keys():
    keys_section_list.append(item)