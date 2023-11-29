from aiogram import Dispatcher, types
from keyboards import client_kb  

dp = Dispatcher

@dp.message_handler(commands=['start'])  
async def start(message: types.Message):
    await message.answer("Привет!", reply_markup=client_kb.start_keyboard)  
    
@dp.message_handler()
async def handle_text(message: types.Message):
    if message.text == '/support':
        await message.answer("Форма поддержки")
        
    elif message.text == '/faq':
       await message.answer("Ответы на вопросы")