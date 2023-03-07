import scrapy
from skuuudledemo.items import TescoProduct 


class TescoSpider(scrapy.Spider):
    name = "tescospider"
    allowed_domains = ["tesco.com"]
    start_urls = ["https://www.tesco.com/groceries/en-GB/search?query=milk"]

    def parse(self, response):
        products = response.css("li.product-list--list-item")

        product_item = TescoProduct()

        for product in products:
            product_item['name'] = product.css("div.product-details--wrapper h3 a span::text").get()
            product_item['price'] = product.css("form p::text").get()
            
            yield product_item