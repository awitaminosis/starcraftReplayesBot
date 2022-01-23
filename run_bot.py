from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, admin_powers, common


async def on_startup(_):
    print("I'm online")


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
admin_powers.register_handlers_admin_powers(dp)
common.register_handlers_common(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
