# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ScrapyTestItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class DoubanItem(Item):
    movie_name = Field()
    movie_director = Field()
    movie_writer = Field()
    movie_roles = Field()
    movie_language = Field()
    movie_date = Field()
    movie_long = Field()
    movie_description = Field()

class Doubantop250FilmItem(Item):
    '''doubantop250film'''
    name = Field()
    url = Field()
    director = Field()
    actor = Field()
    nation = Field()
    type = Field()
    releaseDate = Field()
    rate = Field()
    rate_num = Field()
    summary = Field()