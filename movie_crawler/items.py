# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieRaw(scrapy.Item):
    dysfz_url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    post_img = scrapy.Field()
    douban_rating = scrapy.Field()
    douban_url = scrapy.Field()
    imdb_url = scrapy.Field()
