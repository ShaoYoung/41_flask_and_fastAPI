# Задание №4
# �оздать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
# �спользуйте потоки.

import requests
import threading
import os
import time


def readfile(folder, file):
    filename = os.path.join(folder, file)
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
    count = len(content.split())
    print(f"Количество слов в файле {file} {count}. Посчитано за {time.time()-start_time:.2f} секунд")

folder = 'thread'
threads = []
start_time = time.time()

files = os.listdir(folder)
for file in files:
    thread = threading.Thread(target=readfile, args=[folder, file])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
