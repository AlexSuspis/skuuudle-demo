# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TescoProduct(scrapy.Item):
    search_term = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
