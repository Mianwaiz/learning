import scrapy


class MySpider(scrapy.Spider):

    name = "myspider"

    def __init__(self, category=None,
                 username=None, password=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            f"http://www.example.com/categories/{category}"
            ]
