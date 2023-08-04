import json

import fake_headers
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


KEYWORDS = ["Django", "Flask"]
headers_gen = fake_headers.Headers(browser="firefox", os="win")


def get_full_text(url):
    resp = requests.get(url, headers=headers_gen.generate()).text
    soup = BeautifulSoup(resp, "lxml")
    vacancy_text = soup.find('div', class_='g-user-content').text
    return vacancy_text


def main():
    resp_url = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&"  # &items_on_page=50

    response = requests.get(resp_url, headers=headers_gen.generate())
    html_data = response.text

    hh = BeautifulSoup(html_data, "lxml")
    vacancy_list_tag = hh.find_all('div', class_="vacancy-serp-item-body__main-info")

    result = []
    for vacancy in tqdm(vacancy_list_tag):
        title_tag = vacancy.find("a", class_="serp-item__title")
        header = title_tag.text
        link = title_tag['href']
        text = get_full_text(link)

        if all(map(lambda x: x in text or x in header, KEYWORDS)):
            print(f'\nНайдена подходящая вакансия {header}')
            zp = vacancy.find('span', class_="bloko-header-section-2")
            salary = zp.text if zp else 'зарплата не указана'
            tag = vacancy.find('div', class_='vacancy-serp-item-company')
            company_info = tag.find_all('div', class_='bloko-text')
            company_name, adress = company_info[0].text, company_info[1].text
            res = {
                'link': link,
                'salary': salary,
                'company_name': company_name,
                'city': adress
            }
            result.append(res)

    with open(f"job_vacancy.json", "w", newline='', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=3)


if __name__ == "__main__":
    main()
