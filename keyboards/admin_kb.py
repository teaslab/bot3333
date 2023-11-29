from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  

button_ban = KeyboardButton('/ban')

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  
admin_keyboard.add(button_ban)