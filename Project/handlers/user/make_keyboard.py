from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make():
    buttons = [
        KeyboardButton('/payment'),
        KeyboardButton('/qrcode')
    ]

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    # Unboxing https://metanit.com/python/tutorial/3.7.php
    keyboard.row(*buttons)

    return keyboard
