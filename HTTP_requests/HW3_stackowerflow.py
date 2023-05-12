from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import re


def request_today(url: str):
    response = requests.get(url)
    data = response.json()
    for request in data['items']:
        new_url = 'https://stackoverflow.com/questions/' + str(request['question_id'])
        response = requests.get(new_url)
        soup = BeautifulSoup(response.content, "html.parser")
        pattern = r'\<[^>]*\>'
        if soup.find(text='python'):
            print(f'Creation date: {datetime.fromtimestamp(request["creation_date"]).strftime("%d.%m.%Y")}')
            print(f'Response: {re.sub(pattern, "", str(soup.title))}')


if __name__ == '__main__':
    url_today = "https://api.stackexchange.com/2.3/answers?fromdate=1683676800&todate=1683849600&order=desc&sort=activity&site=stackoverflow"
    request_today(url_today)
