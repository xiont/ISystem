# encoding:utf-8
__author__ = 'Administrator'
import json
import re

import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider

from .. import items
from .. import settings


class DmozSpider(RedisSpider):
    name = "bug"
    redis_key = "spider:bug"


    def parse(self, response):
        dict0 = ["CNNVD", "51CTO", "CNVD_web应用漏洞", "CNVD_安全产品漏洞", "CNVD_应用程序漏洞", "CNVD_操作系统漏洞", "CNVD_数据库漏洞",
                 "CNVD_网络设备漏洞", "CNVD_电信行业漏洞", "CNVD_移动互联网漏洞", "CNVD_工控系统漏洞","Seebug","安全客"]  # ,"Seebug"
        CNVD = "__jsluid=194c1577da1f06194150af2f7ed6d53c; bdshare_firstime=1499945595692; JSESSIONID=3FA87EEBBA670B6387877E6E729AD641; __jsl_clearance=1500433490.28|0|HH1tAjSZXEhWa%2B932gT5P%2BulQGg%3D"
        dict = dict0

        nu = 1
        for form in dict:
            if form == "安全客":
                for i in range(0, nu):
                    url = "https://www.anquanke.com/vul?page=" + str(i + 1)
                    yield scrapy.Request(url, callback=self.anquanke_bug, meta={"platform": form},dont_filter = True)
            if form == "CNVD_web应用漏洞":
                for i in range(0, nu):
                    url = "http://www.cnvd.org.cn/flaw/typeResult?max=20&offset=" + str(
                        i * 20) + "&amp%3Bmax=20&typeId=29&amp%3Boffset=240"
                    yield scrapy.Request(url, callback=self.handle_CNVD, meta={"platform": form},
                                         headers={'Cookie': CNVD},dont_filter = True)
            if form == "CNVD_安全产品漏洞":
                for i in range(0, nu):
                    url = "http://www.cnvd.org.cn/flaw/typeResult?max=20&offset=" + str(
                        i * 20) + "&amp%3Bmax=20&typeId=32&amp%3Boffset=240"
                    yield scrapy.Request(url, callback=self.handle_CNVD, meta={"platform": form},
                                         headers={'Cookie': CNVD},dont_filter = True)
            if form == "CNVD_应用程序漏洞":
                for i in range(0, nu):  # 1934
                    url = "http://www.cnvd.org.cn/flaw/typeResult?max=20&offset=" + str(
                        i * 20) + "&amp%3Bmax=20&typeId=28&amp%3Boffset=240"
                    yield scrapy.Request(url, callback=self.handle_CNVD, meta={"platform": form},
                                         headers={'Cookie': CNVD},dont_filter = True)
            if form == "CNVD_操作系统漏洞":
                for i in range(0, nu):
                    url = "http://www.cnvd.org.cn/flaw/typeResult?max=20&offset=" + str(
                        i * 20) + "&amp%3Bmax=20&typeId=27&amp%3Boffset=240"
                    yield scrapy.Request(url, callback=self.handle_CNVD, meta={"platform": form},
                                         headers={'Cookie': CNVD},dont_filter = True)
            if form == "CNVD_数据库漏洞":
                for i in range(0, nu):
                    url = "http://www.cnvd.org.cn/flaw/typeResult?max=20&offset=" + str(
                        i * 20) + "&amp%3Bmax=20&typeId=30&amp%3Boffset=240"
                    yield scrapy.Request(url, callback=self.handle_CNVD, meta={"platform": form},
                                         headers={'Cookie': CNVD},dont_filter = True)
            if form == "CNVD_网络设备漏洞":
                for i in range(0, nu):
                    url = "http://www.cnvd.org.cn/flaw/typeResult?max=20&offset=" + str(
                        i * 20) + "&amp%3Bmax=20&typeId=31&amp%3Boffset=240"
                    yield scrapy.Request(url, callback=self.handle_CNVD, meta={"platform": form},
                                         headers={'Cookie': CNVD},dont_filter = True)
            if form == "CNVD_电信行业漏洞":
                for i in range(0, nu):  # 238
                    url = "http://telecom.cnvd.org.cn/?max=20&offset=" + str(i * 20)
                    yield scrapy.Request(url, callback=self.handle_CNVD_Hangye, meta={"platform": form},
                                         headers={'Cookie': "__jsluid=19ee5ed6adb83da53658ca8bf44294a1"},dont_filter = True)
            if form == "CNVD_移动互联网漏洞":
                for i in range(0, nu):  # 214
                    url = "http://mi.cnvd.org.cn/?max=20&offset=" + str(i * 20)
                    yield scrapy.Request(url, callback=self.handle_CNVD_Hangye, meta={"platform": form},
                                         headers={'Cookie': "__jsluid=5c79deeaccd8968c085848a85869e759"},dont_filter = True)
            if form == "CNVD_工控系统漏洞":
                for i in range(0, nu):  # 51
                    url = "http://ics.cnvd.org.cn/?max=20&offset=" + str(i * 20)
                    yield scrapy.Request(url, callback=self.handle_CNVD_Hangye, meta={"platform": form},
                                         headers={'Cookie': "__jsluid=580daf76b7dc3dffa204dbef810ea0ef"},dont_filter = True)
            if form == "Seebug":
                for i in range(0, nu):  # 2611
                    url = "https://www.seebug.org/vuldb/vulnerabilities?page=" + str(i+1)
                    yield scrapy.Request(url, callback=self.Seebug, meta={"platform": form},dont_filter = True)

    def handle_CNVD(self, response):
        item = items.bug_item()
        All = Selector(response=response).xpath("/html/body/table/tbody/tr")
        for tr in All:
            name = tr.xpath(".//td[1]/a/@title").extract()[0]
            url = "http://www.cnvd.org.cn" + tr.xpath(".//td[1]/a/@href").extract()[0]
            id = re.findall(r"show/(.*)", url)[0]
            time = tr.xpath(".//td[6]/text()").extract()[0]
            platform = response.meta['platform'].split('_')[0]
            type = response.meta['platform'].split('_')[1]

            item["bug_name"] = name
            item["bug_id"] = id
            item["bug_url"] = url
            item["bug_time"] = time
            item["bug_type"] = type
            item["bug_platform"] = platform
            yield item

    def handle_CNVD_Hangye(self, response):
        item = items.bug_item()
        All = BeautifulSoup(response.text).find('tbody').find_all('tr')
        for tr in All:
            name = tr.find_all('td')[0].find('a')['title']
            url = tr.find_all('td')[0].find('a')['href']
            id = url.split('/')[-1]
            time = tr.find_all('td')[5].get_text().lstrip().rstrip()
            platform = response.meta['platform'].split('_')[0]
            type = response.meta['platform'].split('_')[1]
            item["bug_name"] = name
            item["bug_id"] = id
            item["bug_url"] = url
            item["bug_time"] = time
            item["bug_type"] = type
            item["bug_platform"] = platform
            yield item


    def Seebug(self, response):
        item = items.bug_item()
        All = BeautifulSoup(response.text).find('tbody').find_all('tr')
        for tr in All:
            name = tr.find_all('td')[3].find('a').get_text().lstrip().rstrip()
            url = "https://www.seebug.org"+tr.find_all('td')[3].find('a')['href']
            id = tr.find_all('td')[0].find('a').get_text().lstrip().rstrip()
            time = tr.find_all('td')[1].get_text().lstrip().rstrip()
            platform = response.meta['platform']
            type = ""
            item["bug_name"] = name
            item["bug_id"] = id
            item["bug_url"] = url
            item["bug_time"] = time
            item["bug_type"] = type
            item["bug_platform"] = platform
            yield item

    def anquanke_bug(self, response):
        All = BeautifulSoup(response.text).find('tbody').find_all('tr')
        # print(All)
        # All = Selector(response=response).xpath('//*[@id="vul-list"]/div/table/tbody/tr')

        for each in All:  # each ->tr
            name = each.find_all("td")[0].find("a").get_text()
            platform = each.find_all("td")[2].find("span").get_text()
            url = "https://www.anquanke.com" + each.find_all("td")[0].find("a")["href"]
            time = each.find_all("td")[3].get_text()
            id = each.find_all("td")[1].get_text()
            item = items.bug_item()
            item["bug_name"] = name
            item["bug_id"] = id
            item["bug_url"] = url
            item["bug_time"] = time
            item["bug_type"] = ""
            item["bug_platform"] = platform
            yield item
