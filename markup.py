import aiogram
from aiogram import types
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentType

buttons = ['Включить слежение','Выключить слежение','Обучить модель','Показать нарушителей','Заблокировать']
keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main.add(*buttons)

markup_true_false = InlineKeyboardMarkup(row_width=2)
item_true = InlineKeyboardButton(text = 'Начать запись',callback_data = 'buttonTrue')
item_false = InlineKeyboardButton(text = 'Остановить запись',callback_data = 'buttonFalse')
markup_true_false.add(item_true,item_false)
