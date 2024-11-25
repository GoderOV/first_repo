import logging  
import requests  
from aiogram import Bot, Dispatcher, types    
from aiogram.utils import executor

API_TOKEN = 'Y7290191892:AAFmxpVWNtL5cYA-pight6m_f72qCSISKs4'

# Настройка логгирования  
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера  
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработка команды /recipe  
@dp.message_handler(commands=['recipe'])
async def send_recipe_link(message: types.Message):
    recipe_name = message.get_args()
    if not recipe_name:
        await message.answer("Пожалуйста, укажите название рецепта после /recipe. Например: /recipe пицца")
        return

    response = requests.get(f'https://api.edamam.com/search?q={recipe_name}&app_id=Y7290191892:AAFmxpVWNtL5cYA-pight6m_f72qCSISKs4&app_key=Y7290191892:AAFmxpVWNtL5cYA-pight6m_f72qCSISKs4')
    if response.status_code == 200:
        data = response.json()
        if data.get('hits'):
            recipe_url = data['hits'][0]['recipe']['url']
            await message.answer(f"Вот ссылка на рецепт '{recipe_name}': {recipe_url}")
        else:
            await message.answer("Извините, не удалось найти рецепт. Попробуйте другой запрос.")
    else:
        await message.answer("Произошла ошибка при запросе. Пожалуйста, попробуйте позже.")

# Запуск бота  
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)