# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['yifu-chen.com']
    start_urls = ['http://yifu-chen.com']

    def parse(self, response):
        pass
