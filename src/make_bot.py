import os

from data.db import DataBase

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

db = DataBase()
# Also you can use: os.environ['PAYMASTER_TOKEN']
PAYMASTER_TOKEN = "1744374395:TEST:d8c5f9ddcfff53f11a63"
# Also you can use: Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
bot = Bot(token="7434927155:AAEEIXp0_mCDYFRX2mvuoxnBpeFzdTQNgsc")

# Actually used Redis but in order not to 
# create unnecessary problems to run the bot here used MemoryStorage
dp = Dispatcher(bot=bot, storage=MemoryStorage())
