from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make():
    buttons = [
        KeyboardButton('/payment'),
        KeyboardButton('/qrcode'),
        KeyboardButton('/balance')
    ]

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(*buttons)

    return keyboard
