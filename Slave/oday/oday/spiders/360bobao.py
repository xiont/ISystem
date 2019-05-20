# #encoding:utf-8
# __author__ = 'Administrator'
# import scrapy
# from scrapy.spiders import CrawlSpider
# from scrapy.selector import Selector
# import re
# from .. import items
# import datetime
# from .. import settings
# from scrapy_redis.spiders import RedisSpider
# from bs4 import BeautifulSoup
# class DmozSpider(RedisSpider):
#     name = "bobao"
#     allowed_domains = ["360.cn"]
#     # start_urls = [
#     # "http://bobao.360.cn/vul/index?type=all"
#     # ]
#     redis_key = "spider:bobao"
#     def __init__(self):
#         self.i=1
#
#     def parse(self, response):
#         ''' title = Selector(response=response).xpath('//*/header/h1/a')
#         #print title
#         for item in title:
#             print item.xpath('text()').extract()[0].lstrip().rstrip()'''
#         print "sss"
#
#         All = BeautifulSoup(response.text).find_all('tr')
#         print(All)
#         # All = Selector(response=response).xpath('//*[@id="vul-list"]/div/table/tbody/tr')
#
#         for each in All: #each ->tr
#             title = each.find_all("td")[0].find("a").get_text()
#             source = each.find_all("td")[2].find("span").get_text()
#             link = each.find_all("td")[0].find("a").href
#             time0 = each.xpath('div/span[1]/text()').extract()[0];time1 = time0.lstrip().rstrip();time = time1 #"".join(time1.split())
#             num = re.findall(r'(.+?)小时前',str(time1))
#             if num:
#                 now = datetime.datetime.now()
#                 time = now - datetime.timedelta(hours = int(num[0]))
#             num2 = re.findall(r'(.+?)分钟前',str(time1))
#             if num2:
#                 now = datetime.datetime.now()
#                 time = now - datetime.timedelta(minutes = int(num2[0]) )
#             num3 = re.findall(r'(.+?)天前',str(time1))
#             if num3:
#                 now = datetime.datetime.now()
#                 time = now - datetime.timedelta(days = int(num3[0]) )
#
#             item = items.Bug360_Item()
#             item['title'] = title
#             item['source'] = source
#             item['link'] = link
#             item['time'] = time
#             yield item
#         urlp = "http://bobao.360.cn/vul/index?type=all&page="
#         self.i= self.i+1
#         while(self.i <= 5):
#             url = urlp + str(self.i)
#             yield scrapy.Request(url,callback=self.parse,headers={'Cookie':settings.Bobao_Cookie})
#
#
#
