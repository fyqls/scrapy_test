# -*- coding:utf-8 -*-
'''doubantop250film_spider'''
import csv

from scrapy import log, Selector
from scrapy.spider import Spider

from scrapy_test.items import Doubantop250FilmItem


class DoubanTop250FilmSpider(Spider):
    name = 'doubantop250filmspider'
    allowed_domains = ['movie.douban.com']
    download_delay = 1
    start_urls = []

    def start_requests(self):
        base_url = "http://movie.douban.com/top250?start="
        pageNumber = 1
        for pages in range(pageNumber):
            log.msg("crawling page: " + str(pages + 1))
            startNum = pages * 25
            self.start_urls.append(str(base_url) + str(startNum) + "&filter=")

        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="item"]/div[@class="info"]')
        items = []
        for site in sites:
            item = Doubantop250FilmItem()
            item['name'] = str("".join(site.xpath('div[@class="hd"]/a/span[@class="title"]/text()').extract()))
            item['rate'] = str("".join(site.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()))
            item['url'] = str("".join(site.xpath('div[@class="hd"]/a/@href').extract()))
            item['rate_num'] = str(site.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[1])
            item['summary'] = str("".join(site.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()))

            direct_actor = str(site.xpath('div[@class="bd"]/p/text()').extract()[0]).replace("\n", "")
            if direct_actor.__contains__("主演"):
                item['director'] = direct_actor.split("主演")[0].strip().split("导演")[1].strip().replace(":", "")
                print "name: " + str("".join(site.xpath('div[@class="hd"]/a/span[@class="title"]/text()').extract()))
                item['actor'] = direct_actor.split("主演")[1].strip().replace(":", "")
            else:
                item['director'] = direct_actor.split("导演")[1].strip().replace(":", "")
                item['actor'] = 'unknown'

            releaseDate_nation_type = str(site.xpath('div[@class="bd"]/p/text()').extract()[1]).replace("\n", "")
            item['releaseDate'] = releaseDate_nation_type.split("/")[0].strip()
            item['nation'] = releaseDate_nation_type.split("/")[1].strip()
            item['type'] = releaseDate_nation_type.split("/")[2].strip()
            items.append(item)
        return items