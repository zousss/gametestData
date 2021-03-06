# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import scrapy
import time
import datetime
import re
from scrapy.selector import Selector
from selenium import webdriver
from gametestData.items import GametestdataItem,testHistoryItem

class dysySpider(CrawlSpider):
    #用于区别Spider。 该名字必须是唯一的，不可以为不同的Spider设定相同的名字。
    name = "dysySpider"
    start_urls = ['http://www.diyiyou.com/kf/lishi/']
    base_url = 'http://www.diyiyou.com/kf/history/'
    url = 'http://www.diyiyou.com'
    start_date = datetime.date.today()
    end_date = start_date+datetime.timedelta(days=90)
    #start_date = datetime.date(2014,1,1)
    #end_date = datetime.date.today()

    #获取搜索结果内容，并且获取下一页的链接
    def parse(self,response):
        print '[DATE URL]',response.url
        for game in response.xpath('//table/tbody/tr')[1:]:
            game_link = game.xpath('td[1]/a/@href').extract()[0]
            game_operator = game.xpath('tr[2]/text()').extract()[0] if game.xpath('tr[2]/text()').extract() else ''
            game_info = scrapy.Request(game_link,callback=self.parse_game_info)
            game_info.meta['game_operator'] = game_operator
            yield game_info
        for i in range((self.end_date-self.start_date).days+1):
            action_date = self.start_date+datetime.timedelta(days=i)
            page_date = str(action_date.year)+'-'+str(int(action_date.month))+'-'+str(int(action_date.day))
            page_link = self.base_url+page_date+'.html'
            next_page = scrapy.Request(page_link,callback=self.parse)
            yield next_page
        #获取游戏测试历史数据
        for gametest_history in response.xpath('//table/tbody/tr')[1:]:
            print '[HISTORY]'
            testhistoryItem = testHistoryItem()
            game_link = ''.join(gametest_history.xpath('td[1]/a/@href').extract())
            testhistoryItem['url'] = response.url
            testhistoryItem['game_link'] = game_link
            testhistoryItem['game_id'] = re.search(r'.*\/(\d+)\/.*',game_link).group(1)
            testhistoryItem['game_name'] = ''.join(gametest_history.xpath('td[1]/a/text()').extract()).strip()
            testhistoryItem['game_plat'] = ''.join(gametest_history.xpath('td[2]/text()').extract()).strip()
            testhistoryItem['game_testtime'] = ''.join(gametest_history.xpath('td[3]/text()').extract()).strip()
            testhistoryItem['game_testserver'] = ''.join(gametest_history.xpath('td[4]/a/text()').extract()).strip()
            testhistoryItem['game_developer'] = ''.join(gametest_history.xpath('td[5]/text()').extract()).strip()
            testhistoryItem['game_type'] = ''.join(gametest_history.xpath('td[6]/text()').extract()).strip()
            testhistoryItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield testhistoryItem

    def parse_game_info(self,response):
        ##获取游戏信息
        print '[GAME URL]',response.url
        game_operator = response.meta['game_operator']
        game_desc = ''.join(response.xpath('//div[@class="main_wrap"]/div[@class="main_full"]/div[1]/div[@class="kf_n_b"]/text()').extract()).strip()
        for game_info in response.xpath('//div[@class="main_wrap"]/div[@class="main_full"]/div[1]/div[@class="kf_n_a clearfix"]'):
            gametestItem = GametestdataItem()
            gametestItem['url'] = self.url
            gametestItem['game_link'] = response.url
            gametestItem['game_id'] = re.search(r'.*\/(\d+)\/.*',response.url).group(1).strip()
            gametestItem['game_name'] = ''.join(game_info.xpath('div[2]/div[2]/h1/text()').extract()).strip()
            gametestItem['game_plat'] = 'mobile'
            info = game_info.xpath('div[3]/ul/li/text()').extract()
            if len(info):
                gametestItem['game_style'] = info[-3]
                gametestItem['game_frame'] = info[-2]
                gametestItem['game_developer'] = info[-1]
            gametestItem['game_operator'] = game_operator
            gametestItem['game_theme'] = ''
            gametestItem['game_pattern'] = ''
            gametestItem['game_type'] = ''.join(game_info.xpath('div[3]/ul/li[1]/text()').extract()).strip()

            game_history1 = ''.join(game_info.xpath('div[2]/ul/li[11]/div/span/text()').extract()).strip()
            game_history2 = ';'.join(game_info.xpath('div[2]/ul/li[11]/div/div/div/text()').extract()).strip()
            gametestItem['game_history'] = ''

            gametestItem['game_charge'] = ''.join(game_info.xpath('div[3]/ul/li[2]/text()').extract()).strip()

            gametestItem['game_img'] = ''.join(game_info.xpath('div[1]/img/@src').extract()).strip()
            gametestItem['game_vote'] = ''.join(game_info.xpath('div[2]/div[3]/div[3]/span[1]/text()').extract()).strip()
            gametestItem['game_rank'] = ''
            gametestItem['game_desc'] = game_desc
            gametestItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield gametestItem
        #获取测试信息
        #page = response.xpath('//div[@class="main_wrap"]/div/div[1]/div[@class="pagecode"]/a/text()').extract()
        #max_page = page[-2] if len(page) else '0'
        #for i in range(1,int(max_page)+1):
        #    test_link = response.url+'index_'+str(i)+'.html'
        #    test_page = scrapy.Request(test_link,callback=self.parse_test_info)
        #    yield test_page

    def parse_test_info(self,response):
        print '[HISTORY URL]',response.url
        for gametest_history in response.xpath('//table/tbody/tr')[1:]:
            testhistoryItem = testHistoryItem()
            testhistoryItem['url'] = response.url
            testhistoryItem['game_link'] = response.url
            testhistoryItem['game_id'] = re.search(r'.*\/(\d+)\/.*',response.url).group(1)
            testhistoryItem['game_name'] = ''.join(gametest_history.xpath('td[1]/a/text()').extract())
            testhistoryItem['game_plat'] = ''.join(gametest_history.xpath('td[2]/text()').extract())
            testhistoryItem['game_testtime'] = ''.join(gametest_history.xpath('td[3]/text()').extract())
            testhistoryItem['game_testserver'] = ''.join(gametest_history.xpath('td[4]/a/text()').extract())
            testhistoryItem['game_developer'] = ''.join(gametest_history.xpath('td[5]/text()').extract())
            testhistoryItem['game_type'] = ''.join(gametest_history.xpath('td[6]/text()').extract())
            testhistoryItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield testhistoryItem