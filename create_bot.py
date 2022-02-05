from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()
storage = MemoryStorage()

bot = Bot(token=os.getenv("API_TOKEN"))
dp = Dispatcher(bot, storage=storage)
