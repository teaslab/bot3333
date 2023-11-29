from aiogram import Dispatcher, types
import logging

dp = Dispatcher

# Логгирование ошибок
@dp.errors_handler()
async def error_handler(update, exception):
    logging.error(f'Ошибка: {exception}')  
    
# Обработка неизвестных сообщений
@dp.message_handler()
async def unknown_message(msg: types.Message):
    return await msg.reply("Неизвестная команда!")