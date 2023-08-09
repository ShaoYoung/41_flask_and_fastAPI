# Задание №9
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.

# Использовать для асинхронного подхода
# async with aiohttp.ClientSession() as session:
#     async with session.get(url) as response:
#         if response.status == 200:
#             content = await response.read()
#
# filename = os.path.join('images', filename)
#                 async with aiofiles.open(filename, 'wb') as f:
#                     await f.write(content)

import threading
import multiprocessing
import asyncio
import time
import os
import re
import requests
import aiohttp
import aiofiles
import argparse


# получить список списков ссылок на изображения
def get_img_url_lists(url, parts):
    response = requests.get(url)
    # print(response.status_code)
    # поиск url изображений
    img_urls = re.findall('img .*?src="(.*?)"', response.text)
    img_urls_lists = []
    # делим список img_urls на несколько списков
    use_count = 0
    # print(len(img_urls))
    for i in range(parts - 1):
        urls_list = img_urls[i * len(img_urls) // parts:(i + 1) * len(img_urls) // parts - 1]
        img_urls_lists.append(urls_list)
        use_count += len(urls_list)
    #     print(len(urls_list))
    # print(use_count)
    # print(len(img_urls) - use_count)
    urls_list = img_urls[use_count: len(img_urls)]
    use_count += len(urls_list)
    # print(use_count)
    img_urls_lists.append(urls_list)
    return img_urls_lists


def download_images(pre_folder, mode, img_urls):
    if mode:
        dir_name = pre_folder + '_images_thread'
    else:
        dir_name = pre_folder + '_images_process'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    # total_start_time = time.time()
    for img_url in img_urls:
        if 'http' in img_url:
            filename = img_url.rsplit('/', 1)[1]
            start_time = time.time()
            # на всякий случай. поиск по регулярному выражению не гарантирует 100% результат получения url изображений
            try:
                response = requests.get(img_url)
                # print(filename)
                full_filename = os.path.join(dir_name, filename)
                with open(full_filename, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {img_url} in {time.time() - start_time:.2f} seconds")
            except Exception as err:
                pass


def download_images_threads(pre_folder, img_urls_lists):
    threads = []
    total_start_time = time.time()
    for img_urls_list in img_urls_lists:
        thread = threading.Thread(target=download_images, args=[pre_folder, True, img_urls_list])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return f'Total download time {pre_folder} (threads) - {time.time() - total_start_time:.2f} seconds.'


def download_images_processes(pre_folder, img_urls_lists):
    processes = []
    total_start_time = time.time()
    for img_urls_list in img_urls_lists:
        p = multiprocessing.Process(target=download_images, args=(pre_folder, False, img_urls_list))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    return f'Total download time {pre_folder} (process) - {time.time() - total_start_time:.2f} seconds.'


async def download_images_async(pre_folder, img_urls):
    dir_name = pre_folder + '_images_async'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    # total_start_time = time.time()
    for img_url in img_urls:
        if 'http' in img_url:
            filename = img_url.rsplit('/', 1)[1]
            start_time = time.time()
            # на всякий случай. поиск по регулярному выражению не гарантирует 100% результат получения url изображений
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(img_url) as response:
                        if response.status == 200:
                            content = await response.read()

                full_filename = os.path.join(dir_name, filename)
                async with aiofiles.open(full_filename, 'wb') as f:
                    await f.write(content)
                print(f"Downloaded {img_url} in {time.time() - start_time:.2f} seconds")
            except Exception as err:
                pass


async def download_images_asyncs(pre_folder, img_urls_lists):
    total_start_time = time.time()
    tasks = [asyncio.create_task(download_images_async(pre_folder, img_urls)) for img_urls in img_urls_lists]
    await asyncio.gather(*tasks)
    return f'Total download time {pre_folder} (async) - {time.time() - total_start_time:.2f} seconds.'


def main_download(urls):
    # кол-во частей, на которые будет разбита закачка изображений с каждого url
    parts = 5
    for url in urls:
        # print(url)
        pre_folder = url.replace('/', '').replace(':', '_').replace('.', '_')
        # print(pre_folder)
        img_urls_lists = get_img_url_lists(url, parts)
        # print(img_urls_lists)
        print(download_images_threads(pre_folder, img_urls_lists))
        print(download_images_processes(pre_folder, img_urls_lists))
        print(asyncio.run(download_images_asyncs(pre_folder, img_urls_lists)))


def parser():
    parser = argparse.ArgumentParser(description='Our parser')
    parser.add_argument('url', metavar='F', type=str, nargs='*', help='Please, enter url.')
    args = parser.parse_args()
    main_download(args.url)


if __name__ == '__main__':
    parser()

#     Examples
'''
python sem_4_9.py C:/Users/Nikita/PycharmProjects/41_flask_and_fastAPI/seminars/seminar_4
python sem_4_9.py http://lenta.ru/
python sem_4_9.py http://gb.ru/ https://news.sportbox.ru/
'''


