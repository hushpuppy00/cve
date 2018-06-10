# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request
from cve.items import CveItem
import xlrd

class CvedemoSpider(scrapy.Spider):
    name = 'cvedemo'
    allowed_domains = ['cve.mitre.org']
    filename = r'1.xlsx'
    try:
        book = xlrd.open_workbook(filename)
        sheet0 = book.sheet_by_index(0)
        start_urls = ['http://cve.mitre.org/cgi-bin/cvename.cgi?name='+cve for cve in sheet0.col_values(0)]
        # for url in start_urls:
        #     print('\033[1;32;m')
        #     print(url)
        #     print('\033[0m')
    except ImportError as execlerror1:
        print('\033[1;33;m')
        print('While read the excel error!!! ERROR:%s'%execlerror1)
        print('\033[0m')



    def parse(self, response):
        selector = Selector(response)
        item = CveItem()
        try:
            table = selector.xpath('/html')
            for each in table:
                item['url'] = ",".join(each.xpath('//li/a/@href').extract())
                # print(type(item['url']))
                yield item
        except ImportError as xpatherrro:
            print('\033[1;33;m')
            print('Xpath error!!! ERROR:%s'%xpatherrro)
            print('\033[0m')
        print(item['url'])