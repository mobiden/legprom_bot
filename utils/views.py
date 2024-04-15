import aiogram  # импорт библиотеки aiogram для работы с Telegram Bot API
from aiogram import Bot, types  # импорт классов Bot и типов сообщений
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # импорт хранилища состояний в памяти
from aiogram.dispatcher import Dispatcher  # импорт диспетчера для обработки событий
#import aiofiles  # для асинхронной работы с файлами
from moviepy.editor import VideoFileClip
import os
from settings import BASE_DIR, BOT_TOKEN, create_logs
from utils.get_fabric_script import get_fabric


# инициализируем бота с токеном и хранилище состояний
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())




# обработчик команды старт
@dp.message_handler(commands=['start', 'старт'])
async def start(message: types.Message):
    create_logs(f'bot starting', printing=True)
    await message.reply("Добрый день! Введите, пожалуйста номера признаков до 1000 через пробел:")

# Обрабатываем ответ пользователя
@dp.message_handler()
async def response_processing(message: types.Message):
    create_logs(f'get message', printing=True)
    temp_list = (message.text).split()
    create_logs(f'message: {message.text}', printing=True)
    f_list = []
    for f in temp_list:
        try:
            fi = int(f.strip())
        except:
            await message.reply("Введите, пожалуйста только номера признаков до 1000 через пробел:")
            break
        if fi > 1000:
            await message.reply("Введите, пожалуйста только номера признаков до 1000 через пробел:")
        f_list.append(fi)
    await message.reply(get_fabric(f_list))


# Функция для обработки Webhook
async def on_startup(dispatcher):
    await bot.set_webhook('https://komlyakov.ru/legprom-bot')

# Функция для обработки запросов Webhook
async def on_shutdown(dispatcher):
    await bot.delete_webhook()


#@dp.message_handler()
#async def check_answer(message: types.Message):
#    if message.text in ANSWERS:
#        await message.reply(f'Отличный выбор! {message.text} - прекрасный цвет.')
#    else:
#        await message.reply('К сожалению, такого варианта нет. Давай попробуем еще раз?')
#        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#        keyboard.add(*[types.KeyboardButton(answer) for answer in ANSWERS])
 #       await message.reply(QUESTION, reply_markup=keyboard)


# Обрабатываем ответ пользователя
#@dp.message_handler()
#async def check_answer(message: types.Message):
 #   if message.text in ANSWERS:
#       await message.reply(f'Отличный выбор! {message.text} - прекрасный цвет.')
#    else:
#        await message.reply('К сожалению, такого варианта нет. Давай попробуем еще раз?')
#        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#        keyboard.add(*[types.KeyboardButton(answer) for answer in ANSWERS])
 #       await message.reply(QUESTION, reply_markup=keyboard)




