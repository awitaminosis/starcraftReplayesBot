from aiogram.utils import executor
from create_bot import dp, bot
from handlers import client, admin, admin_powers, common
from data_base import sqlite_db
from dotenv import load_dotenv
import os


load_dotenv()


async def on_startup(dp):
    print("I'm online")
    await bot.set_webhook(os.getenv('URL_APP'))
    sqlite_db.sql_start(os.environ.get('DATABASE_URL'))


async def on_shutdown(dp):
    global base, cur
    await bot.delete_webhook()
    await sqlite_db.shutdown()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
admin_powers.register_handlers_admin_powers(dp)
common.register_handlers_common(dp)

# executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=False,
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 5000))
)