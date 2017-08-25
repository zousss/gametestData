# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import scrapy
import time
import re
import datetime
from gametestData.items import GametestdataItem,testHistoryItem

class ninegameSpider(CrawlSpider):
    #用于区别Spider。 该名字必须是唯一的，不可以为不同的Spider设定相同的名字。
    name = "dangleSpider"
    start_urls = ['http://ng.d.cn/channel/testlist.html']
    base_url = 'http://ng.d.cn/channel/testlist.html'

    #获取搜索结果内容，并且获取下一页的链接
    def parse(self,response):
        for game_info in response.xpath('//div[@id="wrap"]/div[4]/table/tr'):
            testhistoryItem = testHistoryItem()
            testhistoryItem['url'] = self.base_url
            game_link = ''.join(game_info.xpath('td[1]/a/@href').extract())
            testhistoryItem['game_link'] = game_link
            testhistoryItem['game_id'] = re.search(r'.*\/(.*?)\/$',game_link).group(1).strip()
            testhistoryItem['game_name'] = ''.join(game_info.xpath('td[1]/a/@title').extract()).strip()
            testhistoryItem['game_plat'] = ''
            testhistoryItem['game_testtime'] = str(time.localtime().tm_year)+'-'+''.join(game_info.xpath('td[3]/text()').extract()).strip()
            testhistoryItem['game_testserver'] = ''.join(game_info.xpath('td[4]/text()').extract()).strip()
            testhistoryItem['game_developer'] = ''
            testhistoryItem['game_type'] = ''.join(game_info.xpath('td[2]/text()').extract()).strip()
            testhistoryItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield testhistoryItem