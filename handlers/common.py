from aiogram import types, Dispatcher


async def echo_send(message: types.Message):
    await message.reply(message.text + ".\n" + "try /start")


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(echo_send)
