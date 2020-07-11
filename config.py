TOKEN = '1068242181:AAEweQqB3Cm3IVu_ftCgqt6c9XIRj_NKeH0'

# webhook settings
WEBHOOK_HOST = 'https://fdc8c1eb65d8.ngrok.io'
WEBHOOK_PATH = '/path/to/api'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
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

