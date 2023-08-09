# Задание №1
# Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте потоки.
# Загрузка с использованием Threading

import requests
import threading
from multiprocessing import Process, Pool
import os
import time

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
def download(url):
    response = requests.get(url)
    dir_name = 'proc'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    filename = dir_name + '/' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")

processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
