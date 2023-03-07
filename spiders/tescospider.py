from . import inputdata
import scrapy
from typing import List
from skuuudledemo.items import TescoProduct 



class TescoSpider(scrapy.Spider):
    name = "tescospider"
    allowed_domains = ["tesco.com"]

    #Generate search urls from client items and base url
    start_urls = inputdata.generate_start_urls()

    def get_search_term_from_url(self, start_url: str) -> str:

        #Get search term by selecting substring after '='
        search_term = start_url.split('=')[-1]

        return search_term

    def parse(self, response):
        products = response.css("li.product-list--list-item")

        product_item = TescoProduct()

        for product in products:

            product_item['search_term'] = self.get_search_term_from_url(response.url)
            product_item['name'] = product.css("div.product-details--wrapper h3 a span::text").get()
            product_item['price'] = product.css("form p::text").get()


            yield product_item