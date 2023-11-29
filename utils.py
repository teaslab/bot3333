from aiogram import Bot
from config import ADMIN_ID  

async def send_message_to_admin(text): 
    await bot.send_message(chat_id=ADMIN_ID, text=text)