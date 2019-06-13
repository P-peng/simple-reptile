class UrlManager(object):
    def __init__(self):
        # 存新的url
        self.new_urls = set()
        # 存旧的url
        self.old_urls = set()

    def add_new_url(self, url):
        # 空判断
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        # 拿取一个url，并删除，类似栈
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


