# -*- coding: utf-8 -*-
import scrapy
from CrawlerMeneame_net.CrawlerMeneame.CrawlerMeneame.items import CrawlermeneameIte

class MeneameSpider(scrapy.Spider):
    name = 'Meneame'
    allowed_domains = ['meneame.net']
    start_urls = ['https://www.meneame.net/']

    def parse(self, response):
        print(response.text)
