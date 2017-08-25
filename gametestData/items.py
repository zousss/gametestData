# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GametestdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    game_link = scrapy.Field()
    game_id = scrapy.Field()
    game_name = scrapy.Field()
    game_plat = scrapy.Field()
    game_style = scrapy.Field()
    game_frame = scrapy.Field()
    game_developer = scrapy.Field()
    game_operator = scrapy.Field()
    game_theme = scrapy.Field()
    game_pattern = scrapy.Field()
    game_type = scrapy.Field()
    game_history = scrapy.Field()
    game_charge = scrapy.Field()
    game_vote = scrapy.Field()
    game_rank = scrapy.Field()
    game_img = scrapy.Field()
    game_desc = scrapy.Field()
    record_time = scrapy.Field()

class testHistoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    game_link = scrapy.Field()
    game_id = scrapy.Field()
    game_name = scrapy.Field()
    game_plat = scrapy.Field()
    game_testtime = scrapy.Field()
    game_testserver = scrapy.Field()
    game_developer = scrapy.Field()
    game_type = scrapy.Field()
    record_time = scrapy.Field()
