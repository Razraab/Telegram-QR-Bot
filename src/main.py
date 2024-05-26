import logging
import os
from make_bot import dp
from handlers.user.user_handlers import register_user
from aiogram import executor


def main():
    # You should not use logging if your bot is communicating with multiple users, 
    # it will greatly affect the latency of its responses
    logging.basicConfig(level=logging.INFO, filename='pylog.log')
    register_user(dp)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
