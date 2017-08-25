# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import scrapy
import time
import re
import datetime
from gametestData.items import GametestdataItem,testHistoryItem

class ptbusSpider(CrawlSpider):
    #用于区别Spider。 该名字必须是唯一的，不可以为不同的Spider设定相同的名字。
    name = "ptbusSpider"
    start_urls = ['http://www.ptbus.com/hot/schedule/']
    base_url = 'http://www.ptbus.com/hot/schedule/'
    start_date = datetime.date.today()
    end_date = start_date+datetime.timedelta(days=90)

    #获取搜索结果内容，并且获取下一页的链接
    def parse(self,response):
        for game in response.xpath('//*[@id="Subject"]/div[2]/div[2]/ul/li'):
            game_link = game.xpath('div[2]/a/@href').extract()[0]

            testhistoryItem = testHistoryItem()
            testhistoryItem['url'] = self.base_url
            testhistoryItem['game_link'] = game_link
            testhistoryItem['game_id'] = re.search(r'.*\/(.*)\/',game_link).group(1)
            testhistoryItem['game_name'] = ''.join(game.xpath('div[2]/a/text()').extract()).strip()
            testhistoryItem['game_plat'] = ''
            testhistoryItem['game_testtime'] = ''.join(game.xpath('div[1]/text()').extract()).strip()
            testhistoryItem['game_testserver'] = ''.join(game.xpath('div[3]/text()').extract()).strip()
            testhistoryItem['game_developer'] = ''
            testhistoryItem['game_type'] = ''.join(game.xpath('div[4]/text()').extract()).strip()
            testhistoryItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield testhistoryItem

            game_info = scrapy.Request(game_link,callback=self.parse_game_info)
            yield game_info

    def parse_game_info(self,response):
        print '[game info]',response.url
        for game_info in response.xpath('//div[@class="one_ont"]'):
            gametestItem = GametestdataItem()
            gametestItem['url'] = self.base_url
            gametestItem['game_link'] = response.url
            gametestItem['game_id'] = re.search(r'.*\/(.*)\/',response.url).group(1).strip()
            gametestItem['game_name'] = ''.join(game_info.xpath('div[2]/h2/span/text()').extract()).strip()
            gametestItem['game_plat'] =  ''.join(game_info.xpath('div[2]/ul/li[5]/text()').extract()).strip()
            gametestItem['game_style'] = ','.join(game_info.xpath('div[2]/ul/li[2]/span/text()').extract()).strip()
            gametestItem['game_frame'] = ''
            gametestItem['game_developer'] = ''
            gametestItem['game_operator'] = ''
            gametestItem['game_theme'] = ''
            gametestItem['game_pattern'] = ''
            gametestItem['game_type'] = ''.join(game_info.xpath('div[2]/ul/li[1]/a/text()').extract()).strip()
            gametestItem['game_history'] = ''
            gametestItem['game_charge'] = ''
            gametestItem['game_img'] = ''.join(game_info.xpath('div[1]/img/@src').extract()).strip()
            gametestItem['game_vote'] = ''
            gametestItem['game_rank'] = ''
            gametestItem['game_desc'] = ''.join(game_info.xpath('div[2]/div[2]/p/text()').extract()).strip()
            gametestItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield gametestItem
