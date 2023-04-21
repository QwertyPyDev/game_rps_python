from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API, kb, ikb
import random
import asyncio

PROXY_URL = "http://proxy.server:3128"

bot = Bot(token=TOKEN_API, proxy=PROXY_URL)
dp = Dispatcher(bot)

user_is_win = 0
bot_is_win = 0

options = ['✊', '✋', '✌️']

START_MESSAGE = '''
Привет, это игра камень ножницы бумага!
Выберите свою фишку, чтобы начать играть с ботом😉'''

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=START_MESSAGE, reply_markup=kb)

@dp.message_handler(text=['✊', '✋', '✌️'])
async def command_game(message: types.message):
    global user_is_win, bot_is_win
    choice = random.choice(options)
    if message.text == choice:
        await asyncio.sleep(0.5)
        draw = f'''Ничья, бот:{choice} •  Вы:{message.text} - ⏳счет: {user_is_win}:{bot_is_win}'''
        await bot.send_message(chat_id=message.from_user.id, text=draw, reply_markup=ikb)
    elif message.text == '✊' and choice == '✌️' or message.text == '✋' and choice == '✊' or message.text == '✌️' and choice == '✋':
        await asyncio.sleep(0.5)
        user_is_win += 1
        user_win = f'''Вы выиграли, бот:{choice} •  Вы:{message.text} - ⏳счет: {user_is_win}:{bot_is_win}'''
        await bot.send_message(chat_id=message.from_user.id, text=user_win, reply_markup=ikb)
    else:
        await asyncio.sleep(0.5)
        bot_is_win += 1
        bot_win = f'''Бот выиграл, бот:{choice} •  Вы:{message.text} - ⏳счет: {user_is_win}:{bot_is_win}'''
        await bot.send_message(chat_id=message.from_user.id, text=bot_win, reply_markup=ikb)

@dp.callback_query_handler()
async def reset_check(callback: types.callback_query):
    global user_is_win, bot_is_win
    if callback.data == 'reset_check':
        user_is_win = 0
        bot_is_win = 0
        await callback.message.edit_text(f'🔄счет сброшен: {user_is_win}:{bot_is_win}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
