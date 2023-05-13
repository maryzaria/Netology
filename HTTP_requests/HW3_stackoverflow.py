from datetime import datetime, timedelta, date
import requests
from bs4 import BeautifulSoup
import re


class StackOverflowParse:
    def __init__(self, nums_of_days: int):
        self.tags = ['python']
        self.days = nums_of_days
        self.end_date = int(datetime.today().timestamp())
        self.start_date = int((datetime.today() - timedelta(days=nums_of_days)).timestamp())
        self.result = []

    def request_from_answers(self):
        url = "https://api.stackexchange.com/2.3/answers"
        params = {
            "fromdate": str(self.start_date),
            "todate": str(self.end_date),
            "order": 'desc',
            'sort': 'activity',
            'site': 'stackoverflow'
        }
        response = requests.get(url, params=params).json()
        for resp in response['items']:
            new_url = 'https://stackoverflow.com/questions/' + str(resp['question_id'])
            reply = requests.get(new_url)
            soup = BeautifulSoup(reply.content, "html.parser")
            pattern = r'\<[^>]*\>'
            if soup.find(text='python'):
                self.result.append({
                    'Title:': re.sub(pattern, "", str(soup.title)),
                    'Link:': new_url,
                    'Creation date:': datetime.fromtimestamp(resp["creation_date"]).strftime("%d.%m.%Y") + '\n'
                })

    def request_from_questions(self):
        url = 'https://api.stackexchange.com/2.2/questions'
        params = {
            "fromdate": str(self.start_date),
            "todate": str(self.end_date),
            "order": 'desc',
            'sort': 'activity',
            'tagged': ';'.join(self.tags),
            'site': 'stackoverflow'
        }
        response = requests.get(url, params=params).json()
        result = []
        for item in response['items']:
            self.result.append({
                'Title:': item['title'],
                'Link:': item['link'],
                'Tags:': ', '.join(item['tags']),
                'Creation date:': datetime.fromtimestamp(item['creation_date']).strftime("%d.%m.%Y") + '\n'
            })

    def __str__(self):
        self.request_from_questions()
        if self.result:
            return '\n'.join([' '.join([k, v]) for res in sorted(self.result, key=lambda x: x['Creation date:']) for k, v in res.items()])
        return f"No requests found for the last {self.days} days with the tag 'Python'"


if __name__ == '__main__':
    search = StackOverflowParse(2)
    print(search)