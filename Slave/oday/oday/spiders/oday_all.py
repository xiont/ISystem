# __author__ = 'Administrator'
# import scrapy
# from scrapy.spiders import CrawlSpider
# from scrapy.selector import Selector
# from oday import items
#
# class DmozSpider(scrapy.spiders.Spider):
#     name = "oday2"
#     allowed_domains = ["0daybank.org"]
#     start_urls = [
#     "http://www.0daybank.org/"
#     ]
#     def parse(self, response):
#         ''' title = Selector(response=response).xpath('//*/header/h1/a')
#         #print title
#         for item in title:
#             print item.xpath('text()').extract()[0].lstrip().rstrip()'''
#         All = Selector(response=response).xpath('//*/header')
#         for each in All:
#             time = each.xpath('time/text()').extract()
#             title = each.xpath('h1/a/text()').extract()[0]
#             link0 = each.xpath('h1/a/@href').extract()[0]
#             link ='http://www.0daybank.org/'+link0
#             item = items.OdayItem()
#             for oo in time:
#                 item['time'] = oo
#             #    print oo
#             print title,link
#             item['title'] = title
#             item['link'] = link
#             yield item
#         nexturl = Selector(response=response).xpath('//*[@id="content"]/nav/div[1]/a/@href').extract()[0]
#         yield scrapy.Request(nexturl,callback=self.parse)
#
#         #filename = response.url.split("/")[-2]
#         #with open(filename, 'wb') as f:
#         #    f.write(response.body)
#         def parse_content(self, response):
#             pass
