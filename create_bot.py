from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher(bot)
