# 爬虫主程序

# 爬虫主类
from urllib.parse import unquote

from spider import url_manager, html_downloader, html_parser, html_output
from spider.url_manager import UrlManager


class SpiderMain(object):
    def __init__(self):
        # url管理器
        self.urls = UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parse = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        # 装在第一个url
        print(self.urls)
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # 获取url
                new_url = self.urls.get_new_url()
                # 打印当前爬取的url
                print("craw %d : %s", count, unquote(new_url))
                # 启动下载器
                html_cont = self.downloader.downloader(new_url)
                # html解析器
                new_urls, new_data = self.parse.parse(new_url, html_cont)
                # 收集爬取的url，
                self.urls.add_new_urls(new_urls)
                # 收取爬取的数据
                self.output.collect_data(new_data)

                count = count + 1
                if count == 51:
                    break
            except BaseException as err:
                print()
                print("craw false , error:",err)

        self.output.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)