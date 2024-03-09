from aiogram import Bot, Dispatcher, types, executor
from config import token
import logging, requests
from bs4 import BeautifulSoup


bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def hello(message:types.Message):
    await message.answer(f"Привет {message.from_user.username}, Чтобы получить новости нажимайте /news ")
    

@dp.message_handler(commands="news")
async def news(message:types.Message):
    await message.answer("Отправляю Новости...")
         
    number_news = 0

    for page in range(1, 3):
        url = f'https://stopgame.ru/news/all/p{page}'

        respons = requests.get(url=url)
        # print(respons)

        soup = BeautifulSoup(respons.text,'lxml')
        # print(soup)

        all_news = soup.find_all('div', class_='_content_11mk8_159')
        # print(all_news)


        for news in all_news:
            number_news += 1
            
            # print(f"{number_news}) {news.text}")
            await message.answer(f"{number_news}) {news.text}")


executor.start_polling(dp, skip_updates=True)
