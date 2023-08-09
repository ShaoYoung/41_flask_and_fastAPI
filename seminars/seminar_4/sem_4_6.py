# Задание №6
# �оздать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
# �спользуйте асинхронный подход.

import asyncio
import aiofiles
import os
import time


def readfile(folder, file):
    filename = os.path.join(folder, file)
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
    count = len(content.split())
    print(f"Количество слов в файле {file} {count}. Посчитано за {time.time() - start_time} секунд")

async def readfileasync(folder, file):
    filename = os.path.join(folder, file)
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
    count = len(content.split())
    print(f"Количество слов в файле {file} {count}. Посчитано за {time.time() - start_time} секунд")

async def readfileasync_2(folder, file):
    filename = os.path.join(folder, file)
    async with aiofiles.open(filename, "r", encoding='utf-8') as f:
        content = await f.read()
    count = len(content.split())
    print(f"Количество слов в файле {file} {count}. Посчитано за {time.time() - start_time} секунд")


folder = 'thread'
start_time = time.time()

def sinc(folder, files):
    # start_time = time.time()
    for file in files:
        print(files.index(file), time.time())
        readfile(folder, file)
    # print(f"Посчитано за {time.time() - start_time:.2f} секунд")

async def main():
    tasks = []
    files = os.listdir(folder)
    start_time = time.time()
    for file in files:
        task = asyncio.create_task(readfileasync_2(folder, file))
        # task = asyncio.create_task(readfileasync(folder, file))
        tasks.append(task)
    # запустить одновременно все задачи из tasks
    await asyncio.gather(*tasks)

    print(f"Посчитано за {time.time() - start_time} секунд")



if __name__ == '__main__':
    # files = os.listdir(folder)

    # start_time = time.time()
    # sinc(folder, files)
    # # time.sleep(1)
    # print(f"Посчитано за {time.time() - start_time} секунд")

    asyncio.run(main())


