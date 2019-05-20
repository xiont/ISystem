# import scrapy
# from scrapy.spiders import CrawlSpider
# from scrapy.selector import Selector
# from .. import items
# from scrapy_redis.spiders import RedisSpider
# class DmozSpider(RedisSpider):
#     name = "oday"
#     allowed_domains = ["0daybank.org"]
#     redis_key = "spider:oday"
#     # start_urls = [
#     # "http://www.0daybank.org/"
#     # ]
#     def parse(self, response):
#         ''' title = Selector(response=response).xpath('//*/header/h1/a')
#         #print title
#         for item in title:
#             print item.xpath('text()').extract()[0].lstrip().rstrip()'''
#         All = Selector(response=response).xpath('//*/header')
#         # print All
#         for each in All:
#             time = each.xpath('div/span[1]/a/time/text()').extract()
#             title = each.xpath('.//h2/a/text()').extract()
#             link0 = each.xpath('.//h2/a/@href').extract()
#             link =link0
#             item = items.OdayItem()
#             for oo in time:
#                 item['time'] = oo
#                 print oo
#             for tit in title:
#                 item['title'] = tit
#                 print tit
#             for lin in link:
#                 item['link'] = lin
#                 print lin
#             yield item
#
