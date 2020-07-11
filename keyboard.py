from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from config import section_dict

get_news = KeyboardButton('Получить новости') #button 'Get news'

main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_kb.add(get_news)


inline_main_kb = InlineKeyboardMarkup()
for key, value in section_dict.items():
    inline = InlineKeyboardButton(text=value, callback_data=key)
    inline_main_kb.add(inline)




