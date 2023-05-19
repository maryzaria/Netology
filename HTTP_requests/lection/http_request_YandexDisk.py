import os
from pprint import pprint
import requests
from dotenv import load_dotenv

from ya_disk import YandexDisk

load_dotenv()

TOKEN = os.getenv('TOKEN')


def test_request():
    url = "https://httpbin.org/get"
    params = {"model": "nike123"}
    headers = {"Authorization": "secret - token - 123"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code > 200:
        pprint('request is not successful')
    if response.status_code == 200:
        # pprint(f'response content is {response.content}')  # в байтовом виде
        # pprint(f'response content text is {response.text}')  # в текстовом виде
        pprint(response.json())


if __name__ == '__main__':
    # test_request()
    # reddit = Reddit()
    # pprint(reddit.get_popular_videos())
    yd = YandexDisk(token=TOKEN)
    # pprint(yd.get_files_list())  # получаем список файлов на диске
    yd.upload_file_to_disk("Netology/test/test1.txt", "test.txt")
