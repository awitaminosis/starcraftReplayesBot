from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/zerg')
b2 = KeyboardButton('/protos')
b3 = KeyboardButton('/terran')

# kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

# kb_client.add(b1).add(b2).add(b3) #insert #row(b2, b3)
kb_client.row(b1,b2,b3) #insert #row(b2, b3)