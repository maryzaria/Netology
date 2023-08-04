from urllib.parse import urljoin

import fake_headers
import requests

from bs4 import BeautifulSoup
from datetime import datetime


headers_gen = fake_headers.Headers(browser="firefox", os="win")

KEYWORDS = ['дизайн', 'фото', 'web', 'python']


def get_full_text(url):
    article_response = requests.get(url, headers=headers_gen.generate())
    article = BeautifulSoup(article_response.text, "lxml")
    article_body_tag = article.find("div", id="post-content-body")
    return article_body_tag.text


def main():
    response = requests.get("https://habr.com/ru/all/", headers=headers_gen.generate())
    html_data = response.text

    habr_main = BeautifulSoup(html_data, "lxml")
    article_list_tag = habr_main.find("div", class_="tm-articles-list")
    article_tags = article_list_tag.find_all("article")

    for article_tag in article_tags:
        prev_text = article_tag.find('div', class_='tm-article-body tm-article-snippet__lead').text
        header_tag = article_tag.find("h2")
        header = header_tag.text
        tags_list = article_tag.find('div', class_='tm-article-snippet__hubs').text

        a_tag = header_tag.find("a")
        link = urljoin("https://habr.com", a_tag["href"])

        time_tage = article_tag.find("time")
        publication_dt = datetime.strptime(time_tage["datetime"], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%d.%m.%Y')

        article_text = get_full_text(link)

        for key_word in KEYWORDS:
            if any(map(lambda x: key_word in x.lower(), (prev_text, header, tags_list, article_text))):
                print(f'{publication_dt} - {header} - {link}')
                break


if __name__ == "__main__":
    main()
