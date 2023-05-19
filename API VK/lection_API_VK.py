import os
from pprint import pprint
import pandas as pd
import requests
import time
from dotenv import load_dotenv  # для переменных виртуального окружения

load_dotenv()


"""с помощью group.count можно получать только тысячу запросов, 
потом необходимо указывать смещение
также нужно посылать запрос не чаще 1 раза в 3 секунды (использовать time.sleep())"""


class VkAPIHandler:
    base_url = 'https://api.vk.com/method/'

    def __init__(self, token, version='5.131'):
        self.params = {'access_token': token, 'v': version}

    def get_user_data(self, user_ids):
        url = f'{self.base_url}users.get'
        params = {'user_ids': user_ids}.update(self.params)
        response = requests.get(url, params=params)
        data = response.json()
        return data

    def get_user_data_extended(self, user_ids, fields='bdate,city,followers_count'):
        url = f'{self.base_url}users.get'
        params = {'user_ids': user_ids,
                  'fields': fields,
                  **self.params}
        response = requests.get(url, params=params)
        data = response.json()
        return data

    def search_groups(self, q, sort, count=10):
        url = self.base_url + 'groups.search'
        params = {'q': q, 'sort': sort, 'count': count, **self.params}
        response = requests.get(url, params=params)
        data = response.json()
        return data['response']

    def search_news(self, q):
        url = self.base_url + 'newsfeed.search'
        # news_frame = pd.DataFrame()
        params = {'q': q, 'count': 5, **self.params}
        news = []
        while True:
            time.sleep(0.34)
            response = requests.get(url, params=params)
            data = response.json()['response']
            # news_frame = pd.concat([news_frame, pd.DataFrame(data['items'])])
            news.extend(data['items'])
            if 'next_from' in data:
                params.update({'start_from': data['next_from']})
            else:
                pass
            print(len(news))  # можно записать в csv файл
            # return news


if __name__ == '__main__':
    # with open('token.txt', 'r') as token_file:
    #     token = token_file.readline()
    vk_token = os.getenv('VK_API_TOKEN')
    print(vk_token)
    version = os.getenv('VERSION')

    vk = VkAPIHandler(vk_token, version)
    # data = vk.get_user_data_extended(user_ids='1,2,3')
    # pprint(data)
    # groups = vk.search_groups('python', 6)
    # # print(len(groups['items']))
    # # pprint(groups)
    # pprint(pd.DataFrame(groups['items']))
    news = vk.search_news('авто')
    pprint(news, indent=2)
