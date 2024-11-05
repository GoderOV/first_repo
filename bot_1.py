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
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    dp.run_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('OFF')