import logging

from make_bot import dp

from handlers.user.user_handlers import register_user
from aiogram import executor


def main():
    logging.basicConfig(level=logging.INFO)

    register_user(dp)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
