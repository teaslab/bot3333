from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_support = KeyboardButton('Написать в поддержку')
btn_faq = KeyboardButton('Прочитать FAQ')
btn_back = KeyboardButton('Назад')

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.add(btn_support, btn_faq, btn_back)