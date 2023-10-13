import os
import aiofiles

from .make_keyboard import make
from .qr_creator import create
from make_bot import bot, db, PAYMASTER_TOKEN

from handlers.FSMContext import FSMContext
from aiogram import types, Dispatcher


START_MESSAGE = """
Hi this is a bot to create qr codes!
I'm ready to help you with this for a small payment,
but as a start i'm ready to give you 5 attempts👌 to create a code)


If you want to replenish💵 their number 
let me know with the command /payment
"""


async def start_message(message: types.Message):
    await connect()
    await message.answer(START_MESSAGE, reply_markup=make())


async def connect():
    await db.create_connection()
    await db.create_table('users')


async def process_buy(call: types.CallbackQuery):
    await connect()
    await bot.send_invoice(
        chat_id=call.from_user.id,
        title='Buy attemps package',
        description='This package have a 25 attemps',
        provider_token=PAYMASTER_TOKEN,
        payload='buy_package',
        start_parameter='test_bot',
        currency='rub',
        prices=[types.LabeledPrice(label="Attemps Package", amount=100*100)]
    )


async def process_precheck(precheck: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(precheck.id, ok=True)


async def successfuly_payment(message: types.Message):
    await connect()
    print('Success Payment')
    await db.update_user(message.from_user.id, await db.get_attemps(message.from_user.id) + 25)
    await message.answer('You success buy a attemps package!')


async def qrcode_handle(message: types.Message, state: FSMContext):
    await connect()
    path = os.getcwd() + f'\\qrcodes\\{message.from_user.id}'
    if not os.path.exists(path):
        os.mkdir(path)

    create(message.text, path+'\\edited_photo.png')
    async with aiofiles.open(path+'\\edited_photo.png', 'rb') as f:
        await bot.send_photo(chat_id=message.chat.id,
                             photo=await f.read(),
                             caption='Your QR code')
    await FSMContext.next()
    await db.update_user(message.from_user.id, await db.get_attemps(message.from_user.id) - 1)


async def start_dialog(message: types.Message):
    await connect()
    if await db.get_attemps(message.from_user.id) > 0:
        await FSMContext.dialog.set()
        await message.answer('Send text for handle')
    else:
        await message.answer('You haven\'t attemps for create qrcode!'
                             'Please use /payment command')


def register_user(dp: Dispatcher):
    dp.register_message_handler(start_message, commands='start', state=None)
    dp.register_message_handler(process_buy, commands='payment', state=None)
    dp.register_pre_checkout_query_handler(process_precheck, lambda query: True, state=None)
    dp.register_message_handler(successfuly_payment, content_types=types.ContentTypes.SUCCESSFUL_PAYMENT, state=None)
    dp.register_message_handler(start_dialog, commands='qrcode', state=None)
    dp.register_message_handler(qrcode_handle, state=FSMContext.dialog)
