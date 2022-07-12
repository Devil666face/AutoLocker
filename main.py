import config, os

from aiogram import Bot,Dispatcher,types,executor
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

from markup import keyboard_main, markup_true_false
from learning import *
from database import *
from reco import *
from control import *
from unlocker import *

bot = Bot(token=config.TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)

@dp.message_handler(commands = ['start'],state=None)
async def start(message: types.Message):
    await message.answer('Здорова отец',reply_markup=keyboard_main)

@dp.message_handler(Text(equals='Включить слежение'))
async def activate(message: types.Message,state: FSMContext):
    await message.answer('Включаю режим слежения',reply_markup=keyboard_main)
    update_detect_state(True)
    take_reco_thread()

@dp.message_handler(Text(equals='Выключить слежение'))
async def deactivate(message: types.Message,state: FSMContext):
    await message.answer('Выключаю режим слежения',reply_markup=keyboard_main)
    update_detect_state(False)

@dp.message_handler(Text(equals='Показать нарушителей'))
async def show_photo(message: types.Message,state: FSMContext):
    await message.answer('Показываю нарушителей',reply_markup=keyboard_main)
    images = os.listdir("no_success")
    for image in images:
        await bot.send_photo(message.from_user.id,open(f'no_success/{image}','rb'))
    clear_folder("no_success")

@dp.message_handler(Text(equals='Заблокировать'))
async def lock(message: types.Message,state: FSMContext):
    await message.answer('Блокирую компьютер',reply_markup=keyboard_main)
    lock_system()
    update_unlock_state(True)
    take_unlock_thread()

@dp.message_handler(Text(equals='Обучить модель'))
async def lock(message: types.Message,state: FSMContext):
    await message.answer('Выберите действие',reply_markup=markup_true_false)

@dp.callback_query_handler(text_contains="buttonTrue")
async def check(call: types.CallbackQuery):
    update_screen_state(True)
    take_screen_thread()

@dp.callback_query_handler(text_contains="buttonFalse")
async def check(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    update_screen_state(False)
    await bot.send_message(call.from_user.id, f'Ожидайте я обучаюсь по {len(os.listdir("screen"))} скриншотам')
    train_model()
    clear_folder("screen")

if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as ex:
        print(ex)