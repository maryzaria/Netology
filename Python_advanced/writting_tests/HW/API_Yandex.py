import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
print(token)
class YandexDiscUpload:
    def __init__(self, yd_token=token):
        self._headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {yd_token}'
        }

    def create_new_folder(self, folder_name, url='https://cloud-api.yandex.net/v1/disk/resources'):
        params = {'path': folder_name}
        req = requests.put(url, params=params, headers=self._headers)
        return req.status_code


if __name__ == '__main__':
    yd = YandexDiscUpload('y0_AgAAAAAWWe1CAADLWwAAAADjA8alpSHM4m94SgCvFVDVU-XtWXPzyoY')
    print(yd.create_new_folder(list()))
