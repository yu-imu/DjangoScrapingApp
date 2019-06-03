# coding: UTF-8
# you shild use python3.x
import urllib.request, urllib.error
# sholud "pip3 install beautifulsoup4"
import os.path
from bs4 import BeautifulSoup

url = "https://ramendb.supleks.jp/search?q=%E3%83%A9%E3%83%BC%E3%83%A1%E3%83%B3%E4%BA%8C%E9%83%8E&state=hokkaido"

try:
    with urllib.request.urlopen(url=url) as html:
        body = BeautifulSoup(html, "html.parser")
        # 必要なURLだけ格納しよう
        print(body)

except urllib.error.HTTPError as e:
    # Status codeでエラーハンドリング
    if e.code >= 400:
        print(e.reason)
    else:
        raise e
