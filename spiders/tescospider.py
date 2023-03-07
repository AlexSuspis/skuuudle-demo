import scrapy


class TescospiderSpider(scrapy.Spider):
    name = "tesco"
    allowed_domains = ["tesco.com"]
    start_urls = ["https://www.tesco.com/groceries/en-GB/search?query=milk"]

    def parse(self, response):
        # products = response.xpath("//li[@class='product-list--list-item']")
        products = response.css("li.product-list--list-item")

        for product in products:
            yield {
                # 'name': product.xpath("//div[@class='product-details--wrapper']//span/text()").get(),
                # 'price':product.xpath("p[contains(text(), '£')]/text()").get(),

                'name': product.css("div.product-details--wrapper h3 a span::text").get(),
                'price':product.css("form p::text").get(),
            }