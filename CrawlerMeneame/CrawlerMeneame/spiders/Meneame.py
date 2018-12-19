# -*- coding: utf-8 -*-
import scrapy
from CrawlerMeneame.items import CrawlermeneameItem

class MeneameSpider(scrapy.Spider):
    name = 'Meneame'
    allowed_domains = ['meneame.net']
    start_urls = ['https://www.meneame.net/']

    def parse(self, response):
        article_list = response.xpath("//div[@class='center-content']//h2")
        for i_item in article_list:
            article_item = CrawlermeneameItem()
            article_item['article'] = i_item.xpath(".//h2[@class='xh-highlight']//a")
            print(article_item)
