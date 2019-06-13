from urllib import parse
from urllib.parse import unquote

baseUrl = "https://baike.baidu.com/item/Java/85979"
itemUrl = "/item/你好呀/848484"

new_full_url = parse.urljoin(baseUrl, itemUrl)
print(new_full_url)

cn_url = "https://baike.baidu.com/item/%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91%EF%BC%9A%E6%9C%AC%E4%BA%BA%E8%AF%8D%E6%9D%A1%E7%BC%96%E8%BE%91%E6%9C%8D%E5%8A%A1/22442459?bk_fr=pcFooter"
print(unquote(cn_url))