# coding=utf-8
import sys

reload(sys)
# python默认环境编码时ascii
sys.setdefaultencoding("utf-8")
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import os
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.log import configure_logging

def get_base_dir():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    return base_dir


class douban_movie_charts_spider(BaseSpider):
    name = "douban_movie_charts"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/chart"]

    def parse(self, response):
        try:
            open("movie_list.html", 'wb').write(response.body)
            movie = open("movie_list.txt", 'wb')
            movie.write("豆瓣电影排行榜: \n")
            sel = Selector(response)
            sites = sel.xpath('//div[@class="article"]/div[@class="indent"]/div/table/tr[@class="item"]')
            for site in sites:
                url = str(site.xpath('td[@valign="top"]/div[@class="pl2"]/a/@href').extract()[0])
                name = str("".join(str(" ".join(site.xpath('td[@valign="top"]/div[@class="pl2"]/a/text()').extract()).replace("\n", "").replace("\s+", "").replace("/", "")).split()))
                movie.write(str(name)+","+str(url) + "\n")
        except:
            pass
        finally:
            movie.close()
