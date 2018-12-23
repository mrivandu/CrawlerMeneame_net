# -*- coding: utf-8 -*-
import scrapy
import re
#from meneame_net.items import MeneameNetItem


class MeneameSpider(scrapy.Spider):
    name = 'meneame'
    allowed_domains = ['meneame.net']
    start_urls = ['https://www.meneame.net', 'https://www.meneame.net/queue', 'https://www.meneame.net/articles', 'https://www.meneame.net/popular', 'https://www.meneame.net/top_visited']

    def parse(self, response):
        try:
            total_pages_url = response.xpath("//div[@class='pages margin']/a[last()-1]").extract()[0]
            total_pages = int(re.findall(r'\d+',total_pages_url)[0])
            for sub_url in self.start_urls:
                for page_num in range(1,total_pages+1):
                    try:
                        if response.xpath("//div[@class='pages margin']/a[@rel='next']/@href").extract()[0] and response.url == sub_url:
                            new_sub_url = sub_url + "?page=" + str(page_num)
                            yield scrapy.Request(new_sub_url,callback=self.sub_parse)
                    except:
                        break
        except:
            pass

    def sub_parse(self,response):
        sub_url_list = response.xpath("//a[@class='comments']/@href").extract()
        for sub_page_url in sub_url_list:
            try:
                new_sub_page_url = 'https://www.meneame.net' + sub_page_url
                print(new_sub_page_url)
                yield scrapy.Request(new_sub_page_url,callback=self.target_parse)
            except:
                continue
    
    def target_parse(self,response):
        pass
        
"""
    def sub_parse(self,response):
        sub_url_list = response.xpath("//div[@class='news-details-main']/a/@href").extract()
        for sub_page in sub_url_list:
            print("https://www.meneame.net"+sub_page)
"""