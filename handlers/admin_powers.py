from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from dotenv import load_dotenv
import os


load_dotenv()
is_adm_powers = False


class FSMAccess(StatesGroup):
    start = State()
    check = State()


def is_adm():
    return is_adm_powers


async def access_start(message: types.Message):
    await FSMAccess.start.set()
    await message.reply('Say the magic word...')
    await FSMAccess.next()


async def access_check(message: types.Message, state: FSMContext):
    global is_adm_powers
    async with state.proxy() as data:
        adm_pass = os.getenv('ADM_PASS')
        if message.text == adm_pass:
            is_adm_powers = True
    await state.finish()


def register_handlers_admin_powers(dp: Dispatcher):
    dp.register_message_handler(access_start, commands=['adm'], state=None)
    dp.register_message_handler(access_check, state=FSMAccess.check)
