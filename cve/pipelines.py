# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt
from openpyxl import Workbook


class CvePipeline(object):
    def process_item(self, item, spider):
        # 以追加的方式打开文件，不存在则创建
        # 因为item中的数据是unicode编码，为了在控制台中查看数据的有效性和保存，
        # 将其编码改为utf-8
        with open('res.txt', 'a') as f:
            f.write(item['url'] + '\n')

        return item
