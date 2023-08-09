# Асинхронный подход

import asyncio


async def count():
    print("Начало выполнения")
    await asyncio.sleep(1)
    print("Прошла 1 секунда")
    await asyncio.sleep(2)
    print("Прошло еще 2 секунды")
    return "Готово"


async def main():
    # вместе. одновременный запуск три раза
    result = await asyncio.gather(count(), count(), count())
    print(result)

# создание цикла событий с корутиной main
asyncio.run(main())
