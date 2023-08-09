# Задание №7
# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

# глобальная переменная
# lock
# доступ каждого процесса к глобальной переменной
# разделить список срезами

from random import randint
import threading
import multiprocessing
import asyncio
import time

LEN_ARRAY = 1_000_000
MIN_VALUE = 1
MAX_VALUE = 100

sum_threads = 0
# переменная, которая может быть использована в разных процессах
sum_processes = multiprocessing.Value('i', 0)
sum_asyncs = 0


# создаёт список списков. общий размер = LEN_ARRAY
def get_list(count_parts):
    len_arrays = 0
    arrays_list = []
    part = LEN_ARRAY // count_parts
    # print(part)
    for _ in range(count_parts - 1):
        array_list = []
        for _ in range(part):
            array_list.append(randint(MIN_VALUE, MAX_VALUE))
        arrays_list.append(array_list)
        len_arrays += len(array_list)
    # создаём последнюю часть общего списка
    part = LEN_ARRAY - len_arrays
    # print(part)
    array_list = []
    for _ in range(part):
        array_list.append(randint(MIN_VALUE, MAX_VALUE))
    arrays_list.append(array_list)
    len_arrays += len(array_list)
    return arrays_list, len_arrays


def get_sum_thread(array_list):
    global sum_threads
    sum_thread = 0
    for item in array_list:
        sum_thread += item
    sum_threads += sum_thread
    # print(f'Сумма: {sum_thread:_}')


def get_sum_threads(arrays_list):
    global sum_threads
    threads = []
    start_time = time.time()
    for array_list in arrays_list:
        thread = threading.Thread(target=get_sum_thread, args=[array_list])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return f'Calculated (threads) in {time.time() - start_time:.2f} seconds. {sum_threads = }.'


def get_sum_process(sp, array_list):
    sum_process = 0
    for item in array_list:
        sum_process += item
    # на время выполнения блока под with значение переменной sp блокируется в её текущем значении
    with sp.get_lock():
        sp.value += sum_process
    # print(f'Сумма: {sum_process:_}')


def get_sum_processes(arrays_list):
    processes = []
    start_time = time.time()
    for array_list in arrays_list:
        p = multiprocessing.Process(target=get_sum_process, args=(sum_processes, array_list))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    return f'Calculated (processes) in {time.time() - start_time:.2f} seconds. {sum_processes.value = }.'


async def get_sum_async(array_list):
    global sum_asyncs
    sum_async = 0
    for item in array_list:
        sum_async += item
    sum_asyncs += sum_async
    # print(f'Сумма: {sum_async:_}')


async def get_sum_asyncs(arrays_list):
    start_time = time.time()
    tasks = [asyncio.create_task(get_sum_async(array_list)) for array_list in arrays_list]
    await asyncio.gather(*tasks)
    return f'Calculated (async) in {time.time() - start_time:.2f} seconds. {sum_asyncs = }.'


if __name__ == '__main__':
    # кол-во частей общего массива
    count_parts = 10
    arrays_list, len_arrays = get_list(count_parts)
    # print(arrays_list)
    print(f'Количество элементов в {count_parts} подмассивах = {len_arrays:_}')
    print(get_sum_threads(arrays_list))
    print(get_sum_processes(arrays_list))
    print(asyncio.run(get_sum_asyncs(arrays_list)))
