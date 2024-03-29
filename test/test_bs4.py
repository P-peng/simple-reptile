# BeautifulSoup 简单爬虫实例

import re
from bs4 import BeautifulSoup;

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")

print("获取所有的链接")
links = soup.find_all("a")
for link in links:
    print(link)
print("-------------------------------")

print("获取lacie所在超链接")
link_node = soup.find("a", href="http://example.com/lacie")
print(link_node)
print("-------------------------------")

print("正则表达式匹配")
link_node = soup.find("a", href=re.compile("ill"))
print(link_node)
print("-------------------------------")

print("获取p段落文字")
link_node = soup.find("p", class_="title")
print(link_node)
print("-------------------------------")





