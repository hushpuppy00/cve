# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request
from cve.items import CveItem
import xlrd

class CvedemoSpider(scrapy.Spider):

    name = 'cvedemo'
    allowed_domains = ['cnnvd.org.cn']
    filename = r'1.xlsx'
    try:
        book = xlrd.open_workbook(filename)
        sheet0 = book.sheet_by_index(0)
        start_urls = ['http://www.cnnvd.org.cn/web/xxk/ldxqById.tag?CNNVD='+cve for cve in sheet0.col_values(0)]
        # for url in start_urls:
        #     print('\033[1;32;m')
        #     print(url)
        #     print('\033[0m')
    except ImportError as execlerror1:
        print('\033[1;33;m')
        print('While read the excel error!!! ERROR:%s'%execlerror1)
        print('\033[0m')



    def parse(self, response):

        leveldic = {'中危': '中', '高危': '高', '低危': '低', '超危': '高'}
        selector = Selector(response)
        item = CveItem()
        try:
            table = selector.xpath('/html')
            for each in table:
                try:
                    item['cve'] = each.xpath('//body/div[4]/div/div[1]/div[2]/ul/li[3]/a/text()').extract_first().strip()
                except:
                    item['cve'] = 'null'#便于后续故障定位
                try:
                    part1 = each.xpath('//body/div[4]/div/div[1]/div[3]/p[1]/text()').extract_first().strip()
                except:
                    part1 = None
                try:
                    part2 = each.xpath('//body/div[4]/div/div[1]/div[3]/p[2]/text()').extract_first().strip()
                except:
                    part2 = None
                try:
                    if part1 == None and part2 != None:
                        item['abstract'] = part2.strip().replace('CNNVD或','').replace('\r\n','').replace('\n','')
                    elif part2 == None and part1 != None:
                        item['abstract'] = part1.strip().replace('CNNVD或','').replace('\r\n','').replace('\n','')
                    elif part1 != None and part2 != None:
                        item['abstract'] = (part1.strip()+part2.strip()).replace('CNNVD或','').replace('\r\n','').replace('\n','').strip()
                    else:
                        item['abstract'] = 'null'
                except:
                    item['abstract'] = 'null'
                try:
                    item['vulname'] = each.xpath('//body/div[4]/div/div[1]/div[2]/h2/text()').extract_first().strip()
                except:
                    item['vulname'] = 'null'
                try:
                    item['vultime'] = each.xpath('//body/div[4]/div/div[1]/div[2]/ul/li[5]/a/text()').extract_first().strip()
                except:
                    item['vultime'] = 'null'
                try:
                    item['suggest'] = each.xpath('//body/div[4]/div/div[1]/div[4]/p[1]/text()').extract_first().strip() + each.xpath('//body/div[4]/div/div[1]/div[@class="d_ldjj m_t_20"]/p[@class="ldgg"]/text()').extract_first().strip()
                except:
                    item['suggest'] = 'null'
                try:
                    item['refer'] = "https://nvd.nist.gov/vuln/detail/"+each.xpath('//body/div[4]/div/div[1]/div[2]/ul/li[3]/a/text()').extract_first().strip()
                except:
                    item['refer'] = 'null'
                try:
                    item['level'] = leveldic.get(each.xpath('body/div[@class="container m_t_10"]/div/div[@class="fl w770"]/div[@class="detail_xq w770"]/ul/li[2]/a/text()').extract_first().strip())
                except:
                    item['level'] = 'null'
                yield item
                print(part1)
                print(item['abstract'])
        except Exception as xpatherrro:
            print('\033[1;33;m')
            print('Xpath error!!! ERROR:%s'%xpatherrro)
            print('\033[0m')

        # print(item['cve'])
        # print(item['abstract'])
        # print(item['vulname'])
        # print(item['vultime'])
        # print(item['suggest'])
        # print(item['refer'])
        # print(item['level'])