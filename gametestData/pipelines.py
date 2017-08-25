# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings
from gametestData.items import GametestdataItem,testHistoryItem

class GametestdataPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            use_unicode= True,
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if item.__class__ == GametestdataItem:
            try:
                sql = 'INSERT INTO gametestData VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                param = (item['url'],item['game_link'],item['game_id'],item['game_name'],item['game_plat'], \
                         item['game_style'],item['game_frame'],item['game_developer'], \
                         item['game_operator'],item['game_theme'],item['game_pattern'],item['game_type'], \
                         item['game_history'],item['game_charge'],item['game_vote'],item['game_rank'], \
                         item['game_img'],item['game_desc'],item['record_time'])
                self.cursor.execute(sql,param)
                self.connect.commit()
            except pymysql.Warning,w:
                print "Warning:%s" % str(w)
            except pymysql.Error, e:
                print "Error:%s" % str(e)
        if item.__class__ == testHistoryItem:
            try:
                sql = 'INSERT INTO gametestHistory VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                param = (item['url'],item['game_link'],item['game_id'],item['game_name'],item['game_plat'], \
                         item['game_testtime'],item['game_testserver'],item['game_developer'], \
                         item['game_type'],item['record_time'])
                self.cursor.execute(sql,param)
                self.connect.commit()
            except pymysql.Warning,w:
                print "Warning:%s" % str(w)
            except pymysql.Error, e:
                print "Error:%s" % str(e)
        return item
