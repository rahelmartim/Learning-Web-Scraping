# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.crawler import CrawlerProcess

class SpiderScrapy(scrapy.Spider):
    name = "Trybe Spider"
    start_urls  = ['https://blog.betrybe.com/tecnologia/']    
    
    def parse(self, response):
        with open("output.json", "a") as outfile:            
            for post in response.css(".post-outer"):
                item =  dict()
                item['tag'] = post.css(".category-style > .label::text").extract_first()
                item['title'] = post.css(".entry-title > a::text").extract_first()
                item['author'] = post.css(".author > a::text").extract_first()
                
                yield item                                                
                json.dump(item, outfile, ensure_ascii=False)

            next_page = response.urljoin(response.css(".nav-links > .next::attr(href)").extract_first())
            print("*"*50 +'\n' +next_page)
            yield scrapy.Request( url = next_page, callback = self.parse)                