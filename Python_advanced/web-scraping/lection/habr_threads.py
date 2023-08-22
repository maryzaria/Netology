"""div class="tm-articles-list"""
"""
"article"
<h2 class="tm-title tm-title_h2"><a href="/ru/companies/beeline_cloud/articles/751712/" class="tm-title__link" data-test-id="article-snippet-title-link" data-article-link="true"><span>На пороге «нейрозимы» и глобального кризиса — что разработчики систем ИИ думают о будущем технологии</span></a></h2>
"""

"""
<time datetime="2023-08-01T16:29:40.000Z" title="2023-08-01, 19:29">29 минут назад</time>
"""

"""
div id="post-content-body"
"""

from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

import fake_headers
import requests
from bs4 import BeautifulSoup

# параллелит математические расчеты, но не все однозначно
from multiprocessing.pool import Pool

headers_gen = fake_headers.Headers(browser="firefox", os="win")

response = requests.get("https://habr.com/ru/all/", headers=headers_gen.generate())
html_data = response.text

habr_main = BeautifulSoup(html_data, "lxml")
article_list_tag = habr_main.find("div", class_="tm-articles-list")

article_tags = article_list_tag.find_all("article")


def parse_article_tag(article_tag):
    header_tag = article_tag.find("h2")
    a_tag = header_tag.find("a")
    time_tage = article_tag.find("time")

    header_text = header_tag.text

    link = a_tag["href"]
    link = urljoin("https://habr.com", link)
    publication_time = time_tage["datetime"]

    article_response = requests.get(link, headers=headers_gen.generate())
    article = BeautifulSoup(article_response.text, "lxml")
    article_body_tag = article.find("div", id="post-content-body")
    article_body_text = article_body_tag.text

    return {
        "header": header_text,
        "link": link,
        "publication_time": publication_time,
        "article_text": article_body_text[:20],
    }


# чтобы несколько статей парсились одновременно (параллельно)
with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(parse_article_tag, article_tags)
    results = tuple(results)

print(results)
