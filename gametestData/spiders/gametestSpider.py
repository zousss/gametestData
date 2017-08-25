# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import scrapy
import time
import re
import datetime
from gametestData.items import GametestdataItem,testHistoryItem

class gametestSpider(CrawlSpider):
    #用于区别Spider。 该名字必须是唯一的，不可以为不同的Spider设定相同的名字。
    name = "17173Spider"
    start_urls = ['http://newgame.shouyou.com/ceshi.html']
    base_url = 'http://newgame.shouyou.com/ceshi.html'
    start_date = datetime.date.today()
    end_date = start_date+datetime.timedelta(days=90)

    #获取搜索结果内容，并且获取下一页的链接
    def parse(self,response):
        for game in response.xpath('//*[@id="bgitem"]/li'):
            game_link = game.xpath('h6/a/@href').extract()[0]
            game_plat = ','.join(game.xpath('p[3]/span/text()').extract())
            game_operator = ''.join(game.xpath('span/text()').extract())

            testhistoryItem = testHistoryItem()
            testhistoryItem['url'] = self.base_url
            testhistoryItem['game_link'] = game_link
            testhistoryItem['game_id'] = re.search(r'.*-(\d+).*',game_link).group(1)
            testhistoryItem['game_name'] = ''.join(game.xpath('h6/a/@title').extract()).strip()
            testhistoryItem['game_plat'] = game_plat
            testhistoryItem['game_testtime'] = '2017-'+''.join(game.xpath('p[1]/text()').extract()).strip()
            testhistoryItem['game_testserver'] = ''.join(game.xpath('p[2]/text()').extract()).strip()
            testhistoryItem['game_developer'] = ''
            testhistoryItem['game_type'] = ''.join(game.xpath('i[1]/text()').extract()).strip()
            testhistoryItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield testhistoryItem

            game_info = scrapy.Request(game_link,callback=self.parse_game_info)
            game_info.meta['game_plat'] = game_plat
            game_info.meta['game_operator'] = game_operator
            yield game_info


    def parse_game_info(self,response):
        print '[game info]',response.url
        game_operator = response.meta['game_operator']
        game_plat = response.meta['game_plat']
        game_desc = ''.join(response.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/div/div/p[1]/text()').extract()).strip()
        for game_info in response.xpath('//*[@id="content"]/div[1]/div'):
            gametestItem = GametestdataItem()
            gametestItem['url'] = self.base_url
            gametestItem['game_link'] = response.url
            gametestItem['game_id'] = re.search(r'.*-(\d+).*',response.url).group(1).strip()
            gametestItem['game_name'] = ''.join(game_info.xpath('div[2]/h1/text()').extract()).strip()
            gametestItem['game_plat'] =  game_plat
            gametestItem['game_style'] = ','.join(game_info.xpath('div[2]/p[1]/span/text()').extract()).strip()
            gametestItem['game_frame'] = ''
            gametestItem['game_developer'] = ''.join(game_info.xpath('div[2]/table/tbody/tr[1]/td[2]/span/@title').extract()).strip()
            gametestItem['game_operator'] = game_operator
            gametestItem['game_theme'] = ''
            gametestItem['game_pattern'] = ''
            game_type = ''.join(game_info.xpath('div[2]/table/tbody/tr[1]/td[1]/text()').extract()).strip()
            gametestItem['game_type'] = game_type.split(u'：')[1]
            gametestItem['game_history'] = ''.join(game_info.xpath('div[2]/p[2]/text()').extract()).strip()
            gametestItem['game_charge'] = ''
            gametestItem['game_img'] = ''.join(game_info.xpath('div[1]/img/@src').extract()).strip()
            gametestItem['game_vote'] = ''
            gametestItem['game_rank'] = ''
            gametestItem['game_desc'] = game_desc
            gametestItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield gametestItem
