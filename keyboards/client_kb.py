from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b_zvz = KeyboardButton("/zvz")
b_zvt = KeyboardButton("/zvt")
b_zvp = KeyboardButton("/zvp")

b_tvz = KeyboardButton("/tvz")
b_tvt = KeyboardButton("/tvt")
b_tvp = KeyboardButton("/tvp")

b_pvz = KeyboardButton("/pvz")
b_pvt = KeyboardButton("/pvt")
b_pvp = KeyboardButton("/pvp")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b_zvz, b_zvt, b_zvp).row(b_tvz, b_tvt, b_tvp).row(b_pvz, b_pvt, b_pvp)
