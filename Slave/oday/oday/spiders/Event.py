#encoding:utf-8
__author__ = 'Administrator'
import scrapy
from scrapy.spiders import CrawlSpider
import json
from scrapy.selector import Selector
import re
from .. import items
import datetime
from bs4 import BeautifulSoup
from scrapy_redis.spiders import RedisSpider
class DmozSpider(RedisSpider):
    name = "event"
    redis_key = "spider:event"

    def parse(self, response):
        set =["51漏洞","51综合","51新资讯","51新资讯","51云安全","51数据安全","51应用安全","51工控安全","SecWiki安全事件","360安全资讯","SecWiki技术前沿"]
        set = ["51漏洞"]
        platforms = set#set
        nu = 1
        for form in platforms:
            if form == "51综合":
                for i in range(nu):
                    url = "https://other.51cto.com/php/get_channel_recommend_art_list.php?callback=json&page="+str(i)+"&type_id=512&type=recommend&page_size=19"
                    yield scrapy.Request(url, callback=self.handle_51_event, meta={"platform": form},dont_filter = True)
            if form == "51漏洞":
                for i in range(nu):
                    url = "https://other.51cto.com/php/get_channel_recommend_art_list.php?callback=json&page="+str(i)+"&type_id=566&type=recommend&page_size=19"
                    yield scrapy.Request(url, callback=self.handle_51_event, meta={"platform": form},dont_filter = True)
            if form=="51资讯":
                for i in range(nu):
                    url = "http://other.51cto.com/php/get_channel_recommend_art_list.php?callback=json&page="+str(i)+"&type_id=1073&type=recommend&page_size=19"
                    yield scrapy.Request(url,callback=self.handle_51_event,meta = {"platform":form},dont_filter = True)
            if form=="51新资讯":
                for i in range(nu):
                    url = "http://other.51cto.com/php/get_category_new_articles_list.php?callback=json&page="+str(i)+"&type_id=1073"
                    yield scrapy.Request(url,callback=self.handle_51_event,meta = {"platform":form},dont_filter = True)
            if form=="51云安全":
                for i in range(nu):
                    url = "http://other.51cto.com/php/get_category_new_articles_list.php?callback=json&page="+str(i)+"&type_id=1591"
                    yield scrapy.Request(url,callback=self.handle_51_event,meta = {"platform":form},dont_filter = True)
            if form=="51数据安全":
                for i in range(nu):
                    url = "http://other.51cto.com/php/get_category_new_articles_list.php?callback=json&page="+str(i)+"&type_id=1068"
                    yield scrapy.Request(url,callback=self.handle_51_event,meta = {"platform":form},dont_filter = True)
            if form=="51应用安全":
                for i in range(nu):
                    url = "http://other.51cto.com/php/get_category_new_articles_list.php?callback=json&page="+str(i)+"&type_id=516"
                    yield scrapy.Request(url,callback=self.handle_51_event,meta = {"platform":form},dont_filter = True)
            if form=="51工控安全":
                for i in range(nu):
                    url = "http://other.51cto.com/php/get_category_new_articles_list.php?callback=json&page="+str(i)+"&type_id=1668"
                    yield scrapy.Request(url,callback=self.handle_51_event,meta = {"platform":form},dont_filter = True)
            if form== "SecWiki安全事件":
                for i in range(0,nu):
                    url = "https://www.sec-wiki.com/event?Event_page="+str(i)
                    yield scrapy.Request(url,callback=self.SecWiki,meta = {"platform":form})
            if form== "360安全资讯":
                for i in range(0,nu):
                    url = "https://api.anquanke.com/data/v1/posts?size=10&page="+str(i+1)+"&category=news"
                    yield scrapy.Request(url,callback=self.handle_360news,meta = {"platform":form},dont_filter = True)
            if form== "SecWiki技术前沿":
                for i in range(0,nu):
                    url = "https://www.sec-wiki.com/news?ajax=yw0&News_page="+str(i)
                    yield scrapy.Request(url,callback=self.SecWiki,meta = {"platform":form})


    def handle_51_event(self,response):

        data = BeautifulSoup(response.text).find('body').get_text()[6:-4]
        print("data:",data)
        try:
            list = json.loads(data)
            item = items.event_item()
            for content in list:
                item["event_title"] = content['title']
                item["event_time"] = content['stime']
                item["event_url"] = content['url']
                item["event_platform"] = response.meta["platform"]
                yield item

        except:
            pass

    def SecWiki(self,response):
            item = items.event_item()
            All = Selector(response=response).xpath('//*[@id="yw0"]/table/tbody/tr')
            for tr in All:
                time = tr.xpath(".//td/text()").extract()[0]
                title = tr.xpath(".//td[2]/a/text()").extract()[0]
                url0 = tr.xpath(".//td[2]/a/@href").extract()[0]
                url = "https://www.sec-wiki.com"+url0
                item["event_title"] = title
                item["event_time"] = time
                item["event_url"] = url0
                item["event_platform"] = response.meta["platform"]
                yield item

    def handle_360news(self,response):
            item = items.event_item()
            # print(response.text)
            All2 = json.loads(BeautifulSoup(response.text).find("pre").get_text())
            All = json.loads( json.dumps(All2["data"]))
            for li in All:
                title = li['title']
                url = "https://www.anquanke.com/post/id/"+li['id']
                time = li['date']
                item["event_title"] = title
                item["event_time"] = time
                item["event_url"] = url
                item["event_platform"] = response.meta["platform"]
                yield item





