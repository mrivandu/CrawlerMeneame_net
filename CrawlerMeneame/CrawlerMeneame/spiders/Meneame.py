# -*- coding: utf-8 -*-
import scrapy
from CrawlerMeneame.items import CrawlermeneameItem

class MeneameSpider(scrapy.Spider):
    name = 'Meneame'
    allowed_domains = ['meneame.net']
    start_urls = ['https://www.meneame.net/']

    def parse(self, response):
        article_list = response.xpath("//div[@class='center-content']")
        for news_item in article_list:
            article_item = CrawlermeneameItem()
            article_item['article_titile'] = news_item.xpath(".//h2/a/text()").extract_first()
            article_item['article_context'] = news_item.xpath(".//div[@class='news-content']/text()").extract_first()
            print(article_item['article_titile']+'\t'+article_item['article_context'])
