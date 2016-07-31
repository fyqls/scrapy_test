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

# class JsonWriterPipeline(object):
#     def __init__(self):
#         self.file = open('items.jl', 'wb')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item
import os

def get_base_dir():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    return base_dir


class CsvWriterPipeline(object):

    def __init__(self):
        self.csvwriter = csv.writer(open(get_base_dir() + '/movie_top250.csv', 'wb'))
        self.csvwriter.writerow(['电影名称', '链接', '导演', '主演', '国家和地区', '类型', '上映日期', '评分', '评分人数', '剧情简介'])
        # targetFile = os.path.join(get_base_dir(),  "/movie_top250.csv")
        # if os._exists(targetFile) and os.path.isfile(targetFile):
        #     os.remove(targetFile)
        # pass

    def process_item(self, item, spider):
        self.csvwriter.writerow(
            [item['name'], item['url'], item['director'], item['actor'], item['nation'], item['type'],
             item['releaseDate'], item['rate'], item['rate_num'], item['summary']])
        # with open(get_base_dir() + '/movie_top250.csv', 'w+') as f:
        #     f.write('\xEF\xBB\xBF')
        #     self.csvwriter = csv.writer(f)
        #     self.csvwriter.writerow(['电影名称', '链接', '导演', '主演', '国家和地区', '类型', '上映日期', '评分', '评分人数', '剧情简介'])
        #     self.csvwriter.writerow(
        #         [item['name'], item['url'], item['director'], item['actor'], item['nation'], item['type'],
        #          item['releaseDate'], item['rate'], item['rate_num'], item['summary']])
        return item
