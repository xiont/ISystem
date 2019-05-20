# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import settings
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import redis
class MySQLPipeline(object):
    def __init__(self):
        self.r = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=0)
    def process_item(self, item, spider):
        if spider.name=="oday":
            self.r.rpush('item:oday',item)
        if spider.name=="bobao":
            print item
            self.r.lpush('item:bobao',item)
        if spider.name=="event":
            print item
            self.r.rpush('item:event',str(item))
        if spider.name=="bug":
            print(item)
            self.r.rpush('item:bug',str(item))
        return item
