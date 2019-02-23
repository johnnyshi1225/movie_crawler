# -*- coding: utf-8 -*-
import json
from scrapy.exceptions import DropItem


class MovieCrawlerPipeline(object):

    def process_item(self, item, spider):
        # spider.logger.info(item)
        if item.get('title'):
            return item
        else:
            raise DropItem('missing title in item: {}'.format(item))


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
