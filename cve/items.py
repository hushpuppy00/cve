# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cve = scrapy.Field()
    abstract = scrapy.Field()
    vulname = scrapy.Field()
    vultime = scrapy.Field()
    suggest = scrapy.Field()
    refer = scrapy.Field()
    level = scrapy.Field()