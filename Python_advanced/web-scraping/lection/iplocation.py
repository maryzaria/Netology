"""
<strong class="text-underline"><span class="table-ip4-home"> 128.0.240.238</span></strong>
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.iplocation.net/")
html_data = response.text

soup = BeautifulSoup(html_data, "lxml")
span_tag = soup.find("span", class_="table-ip4-home")
ip_addr = span_tag.text.strip()
print(ip_addr)
