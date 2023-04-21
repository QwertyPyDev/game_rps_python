from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN_API = 'YOUR_TOKEN'

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
rock = KeyboardButton(text='✊')
paper = KeyboardButton(text='✋')
scissors = KeyboardButton(text='✌️')
kb.add(rock).insert(paper).add(scissors)

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('⏳ Сбросить счёт', callback_data='reset_check')]
])
