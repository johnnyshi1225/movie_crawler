# -*- coding: utf-8 -*-
import scrapy

from movie_crawler.items import MovieRaw


class DysfzSpider(scrapy.Spider):
    name = 'dysfz'
    allowed_domains = ['www.dysfz.vip']
    start_urls = ['http://www.dysfz.vip/']

    def parse(self, response):
        # parse and follow movie info
        infoList = response.css('ul.movie-list li')
        for info in infoList:
            raw = self._parse_raw_info(info)
            yield raw
        # follow pagination

    def _parse_raw_info(self, info):
        raw = MovieRaw()
        desc = None

        raw['dysfz_url'] = info.xpath('h2/a/@href').extract_first()
        raw['title'] = info.xpath('h2/a/text()').extract_first()

        if info.css('div.des'):
            desc = info.css('div.des')[0]
        if desc:
            raw['post_img'] = desc.xpath('a/img/@src').extract_first()
            # 描述可能会有多行
            if desc.css('div.txt'):
                raw['description'] = ''.join(desc.css('div.txt')[0].xpath('text()').extract())
                outsite_urls = desc.css('div.txt').xpath('p/a[@rel="nofollow"]')
                for url_selector in outsite_urls:
                    url = url_selector.xpath('@href').extract_first()
                    if 'douban' in url:
                        raw['douban_url'] = url
                    elif 'imdb' in url:
                        raw['imdb_url'] = url
                    else:
                        self.logger.warning('unknown outsite url: {}'.format(url))
            if desc.css('span.dbscore'):
                raw['douban_rating'] = desc.css('span.dbscore')[0].xpath('b/text()').extract_first()
        else:
            self.logger.warning('desc part is null')

        return raw
