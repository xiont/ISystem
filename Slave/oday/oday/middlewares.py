__author__ = 'Administrator'
import random
import base64
import datetime
from settings import PROXIES

class RandomUserAgent(object):
    def __init__(self, agents):
        self.agents = agents
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))
    def process_request(self, request, spider):
        print "**************************" + random.choice(self.agents)
        request.headers.setdefault('User-Agent', random.choice(self.agents))

class ProxyMiddleware(object):
    def __init__(self):
        pass
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            print "**************ProxyMiddleware have pass************" + proxy['ip_port']
        else:
            print "**************ProxyMiddleware no pass************" + proxy['ip_port']
            request.meta['proxy'] = "http://%s" % proxy['ip_port']



from selenium import webdriver
from logging import getLogger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
class SeleniumMiddleware(object):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('log-level=3')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')

    def __init__(self,timeout=None,executable_path=''):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.Chrome(executable_path=executable_path,chrome_options=self.options)
        self.browser.set_window_size(1900,1080)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser,self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self,request,spider):
        self.logger.debug("Chorme is Starting")
        try:
            self.browser.get(request.url)
            return HtmlResponse(url=request.url,body=self.browser.page_source,request=request,encoding='utf-8',status=200)
        except:
            return HtmlResponse(url=request.url, status=500, request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   executable_path=crawler.settings.get('CHROME_EXECUTALE_PATH'))