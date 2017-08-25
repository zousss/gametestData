# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import scrapy
import time
import re
import datetime
from gametestData.items import GametestdataItem,testHistoryItem

class ninegameSpider(CrawlSpider):
    #用于区别Spider，同一个项目该名字必须是唯一的。
    name = "9gameSpider"
    start_urls = ['http://www.9game.cn/kc/']
    base_url = 'http://www.9game.cn/kc/'

    #获取搜索结果内容，并且获取下一页的链接
    def parse(self,response):
        for game in response.xpath('//div[@class="des-table"]/div[@class="des-table1"]'):
            day = game.xpath('div[@class="day"]/text()').extract()[0]
            days = str(time.localtime().tm_year)+'-'+'-'.join(re.findall(r'\d+',day))
            for game_info in game.xpath('table/tbody/tr'):
                testhistoryItem = testHistoryItem()
                testhistoryItem['url'] = self.base_url
                game_link = ''.join(game_info.xpath('td[2]/a[1]/@href').extract())
                testhistoryItem['game_link'] = game_link
                testhistoryItem['game_id'] = re.search(r'.*\/(.*?)\/$',game_link).group(1).strip()
                testhistoryItem['game_name'] = ''.join(game_info.xpath('td[2]/a[2]/@title').extract()).strip()
                testhistoryItem['game_plat'] = ','.join(game_info.xpath('td[2]/span/@class').extract()).strip()
                testhistoryItem['game_testtime'] = days+' '+''.join(game_info.xpath('td[1]/span/text()').extract()).strip()
                testhistoryItem['game_testserver'] = ''.join(game_info.xpath('td[3]/text()').extract()).strip()
                testhistoryItem['game_developer'] = ''
                testhistoryItem['game_type'] = ''.join(game_info.xpath('td[4]/text()').extract()).strip()
                testhistoryItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                yield testhistoryItem

                gametestItem = GametestdataItem()
                gametestItem['url'] = self.base_url
                gametestItem['game_link'] = game_link
                gametestItem['game_id'] = re.search(r'.*\/(.*?)\/$',game_link).group(1).strip()
                gametestItem['game_name'] = ''.join(game_info.xpath('td[2]/a[1]/@title').extract()).strip()
                gametestItem['game_plat'] =  ','.join(game_info.xpath('td[2]/span/text()').extract()).strip()
                gametestItem['game_style'] = ''
                gametestItem['game_frame'] = ''
                gametestItem['game_developer'] = ''
                gametestItem['game_operator'] = ''
                gametestItem['game_theme'] = ''
                gametestItem['game_pattern'] = ''
                gametestItem['game_type'] = ''.join(game_info.xpath('td[4]/text()').extract()).strip()
                gametestItem['game_history'] = ''
                gametestItem['game_charge'] = ''
                gametestItem['game_img'] = ''.join(game_info.xpath('td[2]/a[1]/img/@src').extract()).strip()
                gametestItem['game_vote'] = ''.join(game_info.xpath('td[5]/text()').extract()).strip()
                gametestItem['game_rank'] = ''
                gametestItem['game_desc'] = ''
                gametestItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                yield gametestItem