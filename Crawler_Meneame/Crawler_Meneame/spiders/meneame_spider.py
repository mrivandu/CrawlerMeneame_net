# -*- coding: utf-8 -*-
import scrapy


class MeneameSpiderSpider(scrapy.Spider):
    name = 'meneame_spider'
    allowed_domains = ['meneame.net']
    start_urls = ['https://www.meneame.net/']

    def parse(self, response):
        with open('result.text','w') as text_object:
            text_object.writelines(response.text)