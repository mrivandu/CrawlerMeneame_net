# -*- coding: utf-8 -*-
import scrapy
from CrawlerMeneame.items import CrawlermeneameItem


#next_page.xpath=//div[@class='pages margin']/a[@rel='next']/@href

class MeneameSpider(scrapy.Spider):
    name = 'Meneame'
    allowed_domains = ['meneame.net']
    start_urls = ['https://www.meneame.net/']

    def parse(self, response):
        article_list = response.xpath("//div[@class='news-summary']")
        for news_item in article_list:
            article_item = CrawlermeneameItem()
            article_item['article_titile'] = news_item.xpath(".//div[@class='center-content']/h2/a/text()").extract_first()
            article_item['article_context'] = news_item.xpath(".//div[@class='center-content']/div[@class='news-content']/text()").extract_first()
            yield article_item
        next_page = response.xpath("//div[@class='pages margin']/a[@rel='next']/@href").extract()
        if next_page:
            next_page = next_page[1]
            yield scrapy.Request('https://www.meneame.net/'+next_page,callback=self.parse)
