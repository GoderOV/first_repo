import aiogram
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


bot_token = ''


bot = Bot(bot_token)
dp = Dispatcher()


async def main():
    bot = Bot(token='7231784221:AAFAbaYvA15xMj2JagVlzxMmZoSxV68N9rU')
    dp = Dispatcher()
    await dp.start_polling(bot)


@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(f''
                         )


@dp.message(Command(commands=['help']))
async def help_cmd(message: Message):
    await message.answer(f''
                         )


@dp.message(Command(commands=['about']))
async def about_cmd(message: Message):
    await message.answer(f''
                         )


@dp.message(Command(commands='order'))
async def order_cmd(message: Message):
    await message.answer(f''
                         )


@dp.callback_query(F.text == 'Хочу сделать заказ')
async def chose_order(message: Message):
    await message.answer(f''
                         )
























if __name__ == '__main__':
    dp.run_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('OFF')