from pprint import pprint
from datetime import datetime
import requests


def send_data_to_service_company(id_user: int, cwk, hwk, cwb, hwb: float) -> bool:
    """Отправляем данные счетчиков воды в управляющую компанию"""
    url_company = 'https//my.service.company'
    # здесь нужно вставить данные для авторизации
    data = {
        "hot_water_kitchen": hwk,
        "cold_water_kitchen": cwk,
        'cold_water_bathroom': cwb,
        'hot_water_bathroom': hwb,
        'date': datetime.today()
    }
    response = requests.post(url=url_company, data=data)
    if response.status_code > 300:
        raise Exception('Error send_data_to_service_company')
    if response.status_code == 201:
        return True
    return False
# if __name__ == '__main__':
#     try:
#         if send_data_to_service_company():
#             print('Success')
#     except Exception as e:
#         print(e)


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


def test_request1():
    url = "https://httpbin.org/get"
    # params = {"model": "nike123"}
    # headers = {"Authorization": "secret - token - 123"}
    response = requests.get(url)
    if response.status_code > 200:
        pprint('request is not successful')
    if response.status_code == 200:
        pprint(response.json())


if __name__ == '__main__':
    test_request()
    test_request1()
