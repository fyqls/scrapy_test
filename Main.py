# -*- coding: utf-8 -*-

from scrapy import cmdline

if __name__ == '__main__':
    # cmdline.execute("scrapy crawl spider".split())
    cmdline.execute("scrapy crawl doubantop250filmspider".split())