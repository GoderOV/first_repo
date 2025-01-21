import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

API_TOKEN = 'Y7290191892:AAFmxpVWNtL5cYA-pight6m_f72qCSISKs4'

bot = Bot(API_TOKEN)
dp = Dispatcher()


async def main():
    bot = Bot(API_TOKEN)
    dp = Dispatcher()
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(f'Привет, друг! Данный бот поможет тебе/n
                         найти подходящий для тебя рецепт того блюда,/n
                         которое ты хочешь. Для выбора рецепта, сначала/n
                         выбери нужную категорию приёма пищи или повод./n
                         Далее наш помощник-бот предложит тебе подборку/n
                         рецептов подходящих для этой категории. Если же ты/n
                         хочешь найти рецепт просто чтобы перекусить, то/n
                         у нас есть есть библиотека, собранная из 25 рецептов/n
                         на данный момент. Если не нашлось нужного для тебя/n
                         рецепта, то просто предложи его нам и мы его добавим/n
                         в нашу библиотеку, это можно сделать нажав /recomend.'
                         )


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('OFF')