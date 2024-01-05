import scrapy


class GetProductsSpider(scrapy.Spider):
    name = "get_products"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
