from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

import keyboard as kb

from config import TOKEN, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_URL

bot = Bot(TOKEN)
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())

@dp.callback_query_handler(text=['news', 'social'])
async def get_news(callback_query: types.CallbackQuery):
    # await bot.edit_message_text(callback_query.from_user.id)
    # await callback_query.answer('Hello')
    text = 'hello'
    await callback_query.message.edit_text(text)


@dp.message_handler(text='Получить новости')
async def choose_section(message: types.Message):
    await message.reply("Выберите раздел", reply_markup=kb.inline_main_kb)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ бот Дениса Микенина, и я могу "
                        "присылать новости с Тамбовских порталов в удобном для телеграм виде! Подробнее в клавиатуре."
                        "Hello! I am bot from Denis Mikenin and send news from Tambov newspaper", reply_markup=kb.main_kb)



@dp.message_handler()
async def echo(message: types.Message):
    await message.reply('Получите новости кликнув по клавиатуре', reply_markup=kb.main_kb)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    # insert code here to run it before shutdown
    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')



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