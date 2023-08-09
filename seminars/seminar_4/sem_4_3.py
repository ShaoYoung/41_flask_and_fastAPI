# Сравнение разных подходов на примере парсинга сайтов
# Загрузка с использованием asyncio:

import asyncio
# асинхронный модуль для получения информации из сети интернет (асинхронный аналог requests
import aiohttp
import time
import os

urls = ['https://www.google.ru/',
'https://gb.ru/',
'https://ya.ru/',
'https://www.python.org/',
'https://habr.com/ru/all/',
'https://netology.ru',
'https://practicum.yandex.ru',
'https://antiplagiat.ru',
'https://skillbox.ru/',
'https://ru.wikipedia.org/'
]

async def download(url):
    dir_name = 'async'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    # используем класс ClientSession
    async with aiohttp.ClientSession() as session:
        # асинхронно получаем информацию по url
        async with session.get(url) as response:
            text = await response.text()
            filename = dir_name + '/' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

            # async with aiofiles.open(filename, 'wb') as f:
            #     await f.write(content)

async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        # task = asyncio.ensure_future(download(url))
        tasks.append(task)
    # запустить одновременно все задачи из tasks
    await asyncio.gather(*tasks)

start_time = time.time()

if __name__ == '__main__':
    # цикл событий загружаем в loop
    # loop = asyncio.get_event_loop()
    # запустить корутину main до её завершения
    # loop.run_until_complete(main())
    asyncio.run(main())
