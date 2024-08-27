import scrapy


class MySpider(scrapy.Spider):
    name = "myspider"

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        
        # Store all variables from kwargs
        self.category = kwargs.get('category', 'cat')
        self.username = kwargs.get('username', 'waiz')
        self.password = kwargs.get('password', '123')
        print(kwargs)

        self.start_urls = [
            f"http://www.example.com/categories/{self.category}"
        ]
spider = MySpider(super)
