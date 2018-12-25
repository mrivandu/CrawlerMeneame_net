# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from meneame_net.items import MeneameNetItem

class MeneameSpider(scrapy.Spider):
    name = 'meneame'
    allowed_domains = ['meneame.net']
    start_urls = ['https://www.meneame.net']#, 'https://www.meneame.net/queue', 'https://www.meneame.net/articles', 'https://www.meneame.net/popular', 'https://www.meneame.net/top_visited']

    def parse(self, response):
        for sub_url in self.start_urls:
            try:
                sub_url_str = response.xpath("//div[@class='pages margin']/a[last()-1]/@href").extract()[0]
                total_pages = int(re.findall(r'\d+',sub_url_str)[0])
                if response.url == sub_url:
                    for page_num in range(2,total_pages-7668):
                        new_sub_url = sub_url + "/?page=" +str(page_num)
                        yield scrapy.Request(new_sub_url,callback=self.sub_parse)
                else:
                        continue
            except:
                yield scrapy.Request(sub_url,callback=self.sub_parse)
                continue

    def sub_parse(self,response):
        target_url_list = response.xpath("//div[@class='news-details-main']/a[@class='comments']/@href").extract()
        if len(target_url_list) > 0:
            for target_url in target_url_list:
                target_page_url = "https://www.meneame.net" + target_url
                if requests.get(target_page_url).status_code == 200 :
                    yield scrapy.Request(target_page_url,callback=self.target_parse)
                else:
                    continue

    def target_parse(self,response):
        target_root_xpath_list = response.xpath("//div[@id='newswrap']")
        for root_xpath in target_root_xpath_list:
            meneame_item = MeneameNetItem()
            meneame_item['article_titile'] = root_xpath.xpath(".//div[@class='news-summary']/div[@class='news-body']/div[@class='center-content']/h2/a/text()").extract_first()
            meneame_item['article_content'] = root_xpath.xpath(".//div[@class='news-summary']/div[@class='news-body']/div[@class='center-content']/div[@class='news-content']/text()").extract_first()
            meneame_item['article_comment'] = root_xpath.xpath(".//div[@id='comments-top']/div[descendant-or-self::text()]//div[@class='comment-text']/text()").extract()
            yield meneame_item