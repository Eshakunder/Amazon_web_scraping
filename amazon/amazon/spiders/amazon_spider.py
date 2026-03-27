import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    page_number= 2 #pagination 
    start_urls = ["https://www.amazon.in/s?k=books&rh=p_n_publication_date%3A2684819031&dc&crid=LCT2RXL5F5J0&qid=1774509496&rnid=2684818031&sprefix=boo%2Caps%2C460&ref=sr_nr_p_n_publication_date_1&ds=v1%3A7H6h66zQu1%2BDiaxfBJn6SiYPc5L1zHVGKLx88kKYUFM"]

    def parse(self, response):
        items = AmazonItem()
        product_name = response.css("h2::text").extract()
        product_author = response.css('.a-size-base.a-link-normal.s-underline-text.s-underline-link-text.null.s-link-style::text').extract()
        product_price = response.css(".a-price-whole::text").extract()
        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price


        yield items

#pagination code strts here,
        next_page = "https://www.amazon.in/s?k=books&rh=p_n_publication_date%3A2684819031&dc&page=" + str(AmazonSpiderSpider.page_number) + "&xpid=2vfq_R_Ssle9m&crid=3PNCIGMBKLN6Z&qid=1774517733&rnid=2684818031&sprefix=%2Caps%2C464&ref=sr_pg_2"

        AmazonSpiderSpider.page_number += 1
        if AmazonSpiderSpider.page_number <= 20:#how many pages you want to scrape

           yield response.follow(next_page, callback=self.parse)
