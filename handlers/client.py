from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import postgres_db


async def command_start(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id,
            "Greetings Cerebrate! What replays would you like to watch?",
            reply_markup=kb_client,
        )
        await message.delete()
    except:
        await message.reply(
            "An exceptional situation has occurred - there was an exception"
        )


async def command_watch_replay(message: types.Message):
    try:
        # await bot.send_message(message.from_user.id, "Sorry, later. I'm still watching replays myself")
        await postgres_db.sql_read(message, message.text)
    except Exception as e:
        print(str(e))
        await message.reply(
            "An exceptional situation has occurred - there was an exception."
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(
        command_watch_replay,
        commands=["zvz", "zvt", "zvp", "tvz", "tvt", "tvp", "pvz", "pvt", "pvp"],
    )
