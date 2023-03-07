
# skuuudle-demo
A demo for a client scenario where we scrape competitor items of an off-licence store as part of a market study.

---------------
Let us imagine we have a new Skuuudle Client, ***Rusholme Off-licence***.

They are currently conducting a market research into their competitors and would like to know how they are pricing their products. 

This knowledge will help Rusholme Off-license to decide: 1) which products to buy and 2) the price at which they will be sold for maximum profit and competitive advantage.

They have provided us with a list of ***items***, the business viability of which they are considering, as well as a list of ***competitors***, who they wish to gain information on.

For this demo, I have designed and implemented a simple Scrapy solution we might use to obtain some basic information by scraping the website of the competitors for each of the items.

**Disclaimer: The purpose of this solution is to implement a simple proof-of-work solution to learn a bit more about Scrapy, rather than a full professional undertaking.**

----------------
### Screenshot of current output in CSV format
This is the output file when running ```scrapy crawl tescospider -O scraped-tesco-data.csv``` on our Terminal:

![image](https://user-images.githubusercontent.com/38634285/223577903-96fb1460-5fa1-47a0-a7d2-49be70ba36f0.png)

As we can see, with our data in this format, we can very easily feed it into the next stage of our process; whether that's processing it by loading it into a Pandas Dataframe, or store it in our database.

----------------
### Features

- In this solution I have currently implemented a Spider which is designed to crawl Tesco's website. (I have learnt that due to Scrapy being a framework for web scraping, it is simple to create spiders for other competitors, such as Lidl, Aldi, Sainsbury's, etc..)

- I automated the creation of start_urls based on the items and competitors given to us. Given a list of string (items, or search_terms), and a base_search_url, we create the start_urls which our TescoSpider will use.

----------------
### Future work / improvements 
Due to only have had two days to design and implement this solution, as well as learn the Scrapy framework, this software system is a little bit rough around the edge.

Here's a couple of further improvements I would make:
- Create spiders for other competitors such as Aldi, Lidl, Sainsbury's, Morrison's, etc..
  - And for each find the respective css selectors for selecting the elements containing price and item name.
- Add support for edge cases, such as when price element is not displayed due to product being out of stock (Use Scrapy Pipelines)
- Setup MySQL functionality: Initial database connection, a script to create and populate tables with input data, fetching of said input data on creation of our TescoSpider, and saving of scraped data in JSON/CSV format into database.
- Add preprocessing of scraped data using Scrapy Pipelines in order to deal with edge cases such as price not being displayed due to item being out of stock.
- Create web microservice out of application, dockerize into a container and deploy into a kubernetes cluster in AWS, while provisioning infrastructure via Terraform.


### Conclusion
This was a very rewarding and fun introduction to the Scrapy framework, and it re-ignited within me the love for Data Science I had developed throughout my university degree!
I am keen on learning more about Scrapy and mastering this technology.
