import os

from data.db import DataBase

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

db = DataBase()
PAYMASTER_TOKEN = os.environ['PAYMASTER_TOKEN']
bot = Bot(token=os.environ['QR_BOT_TOKEN'])
dp = Dispatcher(bot=bot, storage=MemoryStorage())
