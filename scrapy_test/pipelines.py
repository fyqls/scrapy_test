# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ScrapyTestPipeline(object):
#     def process_item(self, item, spider):
#         return item
import csv
import json

class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class CsvWriterPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        with open('films.csv', 'wb') as f:
            f.write('\xEF\xBB\xBF')
            self.csvwriter = csv.writer(f)
            self.csvwriter.writerow(['电影名称', '链接', '导演', '主演', '国家和地区', '类型', '上映日期', '评分', '评分人数', '剧情简介'])
            self.csvwriter.writerow(item)
        return item