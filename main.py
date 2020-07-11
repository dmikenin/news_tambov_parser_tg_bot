from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook
import datetime

import keyboard as kb

from config import TOKEN, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_URL
from config import keys_section_list

from parser.online_tambov import ParserOnlineTambov

import logging
logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)
bot.parse_mode = 'Markdown'

dp.middleware.setup(LoggingMiddleware())

@dp.callback_query_handler(text=keys_section_list)
async def get_news_from_section(callback_query: types.CallbackQuery):
    parser = ParserOnlineTambov()
    result_parser = parser.call(callback_query.data, callback_query.from_user.id)
    date = datetime.datetime.today()
    await callback_query.message.answer('*Статьи на {date_query}*'.format(date_query=date.strftime('%d.%m.%Y %H:%M')))

    for item in result_parser:
        await callback_query.message.answer(item)

    await callback_query.message.answer('*Новых материалов нет*')  # Dont have new articles


@dp.message_handler(text='Получить новости')
async def choose_section(message: types.Message):
    await message.reply("Выберите раздел", reply_markup=kb.inline_main_kb)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ бот Дениса Микенина, и я могу "
                        "присылать новости с Тамбовских порталов в удобном для телеграм виде! Подробнее в клавиатуре."
                        "Hello! I am bot from Denis Mikenin and send news from Tambov newspaper",
                        reply_markup=kb.main_kb)


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply('Получите новости кликнув по клавиатуре', reply_markup=kb.main_kb)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == "__main__":
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
