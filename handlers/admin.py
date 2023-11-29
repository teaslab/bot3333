from aiogram import Dispatcher, types
from aiogram.types import Message  

dp = Dispatcher

# Логика обработки команд администратора
@dp.message_handler(commands="ban") 
async def ban_user(msg: Message):
    await msg.reply("Заблокировать пользователя")
    
@dp.message_handler(content_types=types.ContentType.TEXT)
async def admin_text(msg: Message):  
    if msg.text.lower() == "привет":
        await msg.answer("Привет админ!")