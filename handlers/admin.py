from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from handlers.admin_powers import is_adm
from data_base import postgres_db


class FSMAdmin(StatesGroup):
    url = State()
    who = State()
    tags = State()
    win = State()


async def cm_start(message: types.Message):
    if is_adm():
        await FSMAdmin.url.set()
        await message.reply("What url?")


# 1
async def load_url(message: types.Message, state: FSMContext):
    if is_adm():
        async with state.proxy() as data:
            data["url"] = message.text
        await message.reply("Who fights?")
        await FSMAdmin.next()


# 2
async def load_who(message: types.Message, state: FSMContext):
    if is_adm():
        async with state.proxy() as data:
            data["who"] = message.text.lower()
        await message.reply("Tags?")
        await FSMAdmin.next()


# 3
async def load_tags(message: types.Message, state: FSMContext):
    if is_adm():
        async with state.proxy() as data:
            data["tags"] = message.text.lower()
        await message.reply("Who wins?")
        await FSMAdmin.next()


# 4
async def load_win(message: types.Message, state: FSMContext):
    if is_adm():
        async with state.proxy() as data:
            data["win"] = message.text.lower()
        async with state.proxy() as data:
            await message.reply(str(data))

        await postgres_db.sql_add_command(state)
        await state.finish()


async def cancel_handler(message: types.Message, state: FSMContext):
    if is_adm():
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply("ok")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cancel_handler, commands=["cancel"], state="*")
    dp.register_message_handler(
        cancel_handler, Text(equals="отмена", ignore_case=True), state="*"
    )

    dp.register_message_handler(cm_start, commands=["upload"], state=None)
    dp.register_message_handler(load_url, state=FSMAdmin.url)
    dp.register_message_handler(load_who, state=FSMAdmin.who)
    dp.register_message_handler(load_tags, state=FSMAdmin.tags)
    dp.register_message_handler(load_win, state=FSMAdmin.win)
