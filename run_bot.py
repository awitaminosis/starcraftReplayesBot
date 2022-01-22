from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, common


async def on_startup(_):
    print("I'm online")


client.register_handlers_client(dp)
# admin.register_handlers_client(dp)
common.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
