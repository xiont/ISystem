# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class OdayItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    time = scrapy.Field()

class Bug360_Item(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    source = scrapy.Field()
    time = scrapy.Field()

class event_item(scrapy.Item):
    event_title = scrapy.Field()
    event_time = scrapy.Field()
    event_url = scrapy.Field()
    event_platform = scrapy.Field()

class bug_item(scrapy.Item):
    bug_name = scrapy.Field()
    bug_id = scrapy.Field()
    bug_time = scrapy.Field()
    bug_url = scrapy.Field()
    bug_platform = scrapy.Field()
    bug_type = scrapy.Field()

class eventMongo(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    time =scrapy.Field()
    url =scrapy.Field()
    platform = scrapy.Field()
