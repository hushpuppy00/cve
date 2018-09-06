# -*- coding: utf-8 -*-
import csv

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CvePipeline(object):

    def __init__(self):
        self.filename = csv.writer(open('result.csv','w'),delimiter=',')
        self.filename.writerow(['漏洞名称(非空)','漏洞中文描述(非空)','CVE编号(选填)','危险等级(非空)','最早公开时间(非空)'
                                '原始信息来源(非空)'])

    def process_item(self,item,spider):
        print('writeing')

        # rows = zip(item['vulname'],item['abstract'],item['cve'],item['level'],item['vultime'],
        #           item['suggest'],item['refer'])
        #
        # for _ in rows:
        #     print(_)
        self.filename.writerow([item['vulname'],item['abstract'],item['cve'],item['level'],item['vultime'],
                  item['suggest'],item['refer']])

        return item
