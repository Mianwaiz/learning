import scrapy


class MySpider(scrapy.Spider):

    name = "myspider"
    username = 'waiz'
    password = 123

    def __init__(self, category=None,
                 username=username, password=password, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            f"http://www.example.com/categories/{category}{username}{password}"
            ]
            
