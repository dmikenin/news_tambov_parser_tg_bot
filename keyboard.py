from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


get_news = KeyboardButton('Получить новости')

main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_kb.add(get_news)


inline_main_kb = InlineKeyboardMarkup()

inline_news = InlineKeyboardButton(text='Новости', callback_data='news')
inline_main_kb.add(inline_news)

inline_social = InlineKeyboardButton('Общество', callback_data='social')
inline_main_kb.add(inline_social)

inline_lch = InlineKeyboardButton('ЖКХ', callback_data='lch')
inline_main_kb.add(inline_lch)

inline_economy = InlineKeyboardButton('Экономика', callback_data='economy')
inline_main_kb.add(inline_economy)

inline_event = InlineKeyboardButton('Проишествия', callback_data='event')
inline_main_kb.add(inline_event)

inline_culture = InlineKeyboardButton('Культура', callback_data='culture')
inline_main_kb.add(inline_culture)

inline_sport = InlineKeyboardButton('Спорт', callback_data='sport')
inline_main_kb.add(inline_sport)




