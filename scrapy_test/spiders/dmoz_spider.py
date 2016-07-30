from scrapy import Selector
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import Spider

from scrapy_test.items import DmozItem


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books.html/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # open(filename, 'wb').write(response.body)
        sel = Selector(response)
        sites = sel.xpath('//div[@class="site-item "]/div[@class="title-and-desc"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/div[@class="site-title"]/text()').extract()
            item['desc'] = site.xpath('div[@class="site-descr "]/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            items.append(item)
            return items
