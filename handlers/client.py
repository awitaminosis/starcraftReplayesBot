from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

async def command_start(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Greetings Cerebrate! What replays would you like to watch?', reply_markup=kb_client)
		# await bot.send_message(message.from_user.id, 'Greetings Cerebrate')
		await message.delete()
	except:
		await message.reply('mesages via direct\n https://t.me/starcraftReplaysBot')

async def open_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'zerg, toss, terran')


async def command_watch_zerg(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, "Sorry, later. I'm still watching zerg's replays myself")
		await message.delete()
	except:
		await message.reply('mesages via direct\n https://t.me/starcraftReplaysBot')

async def command_watch_protos(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, "Sorry, later. I'm still watching protos' replays myself")
		await message.delete()
	except:
		await message.reply('mesages via direct\n https://t.me/starcraftReplaysBot')

async def command_watch_terran(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, "Sorry, later. I'm still watching terran's replays myself")
		await message.delete()
	except:
		await message.reply('mesages via direct\n https://t.me/starcraftReplaysBot')


def register_handlers_client(dp: Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(open_command, commands=['types'])
	dp.register_message_handler(command_watch_zerg, commands=['zerg'])
	dp.register_message_handler(command_watch_protos, commands=['protos'])
	dp.register_message_handler(command_watch_terran, commands=['terran'])
