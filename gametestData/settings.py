# -*- coding: utf-8 -*-

# Scrapy settings for gametestData project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import random

BOT_NAME = 'gametestData'
LOG_LEVEL = 'WARNING'

SPIDER_MODULES = ['gametestData.spiders']
NEWSPIDER_MODULE = 'gametestData.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gametestData (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

def getCookie():
    cookie_list = [
        'SUV=1490956334637848; NUV=1490976000000; OKIDEA_AD_BI_COOKIE_ID=b97aa6a4c4b04da89302ec56576cb3d6; ued_ping_tk182=2,1491042750342; PHPSESSID=9v86u3it2ul8e69ih8c1lt32c1; ued_feature_AdNewgameOnlineGameGift.v1=1; live_17173_unique=5b4afc04dec5dd0f0d8bfb04095b0a95; ued_ping_tknewgame.17173.com=23,1491356617083; ued_ping_tkwww.17173.com=7,1491356689994; Hm_lvt_4dd339463ea8f10d29871edc2cf0f6d1=1491355549,1491356112,1491356493,1491356548; Hm_lpvt_4dd339463ea8f10d29871edc2cf0f6d1=1491357806; DIFF=1491357805574; ONLINE_TIME=1491357805568; ued_ping_ssid=149095633463784814913555637288611491354028751|27; ued_ping_ssid2=149095633463784814913555637288611491354028751|27; IPLOC=CN3301'
    ]
    cookie = random.choice(cookie_list)
    return cookie

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch, br",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
    'Cookie':'%s' % getCookie()
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'gametestData.middlewares.GametestdataSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'gametestData.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'gametestData.pipelines.GametestdataPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = False
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# start MySQL database configure setting
MYSQL_HOST = '192.168.112.47'
MYSQL_DBNAME = 'spiderdata'
MYSQL_USER = 'zoujianwei'
MYSQL_PASSWD = 'KPhUIEd2t622uwtB1xtZ'
# end of MySQL database configure setting