# -*- coding: utf-8 -*-

# Scrapy settings for oday project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html


ITEM_PIPELINES = ['myapp.pipelines.DjangoPipeline']

# http://stackoverflow.com/questions/4271975/access-django-models-inside-of-scrapy

BOT_NAME = 'oday'

SPIDER_MODULES = ['oday.spiders']
NEWSPIDER_MODULE = 'oday.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'oday (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
CONCURRENT_REQUESTS = 128

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
SEEBUG_COOKIE = "__jsluid=bc20ff0699a1a1c147ea2dcbcb889e6f; Hm_lvt_6b15558d6e6f640af728f65c4a5bf687=1500095536; __jsl_clearance=1500432615.739|0|8Amp9bZORTpd9u0nJsNsE6UqiaQ%3D"
EXPLOIT_COOKIE = 'PHPSESSID=44efmbfrmlc2f6i4c6opdkfvb6; __unam=d0030f5-15a72aef977-69e8404-71; _ga=GA1.3.1126361205.1491027434'
Bobao_Cookie = '''test_cookie_enable=null; __huid=10Xsd%2BygxjcI5y0T8cVLmpXKQD5XfJ%2BMdRmoqJ1gSbfKE%3D; __guid=132730903.4084110824650876400.1459517048988.298; _ga=GA1.2.1369358589.1464049213; B=ID=855031487983696:V=2:S=a4babeb716; UM_distinctid=15aa36c36324b9-0ff348909-b0c2725-100200-15aa36c36337cb; __hsid=6b02610b6d972932; PHPSESSID=7qu31g095hf5ui9ilr68oh1831; monitor_count=1; __gid=65863720.727105252.1484370743377.1499689218687.117; __sid=67796994.3960980692221790700.1499689218684.8635; CNZZDATA1253147824=1022319478-1487850171-https%253A%252F%252Fwww.baidu.com%252F%7C1499684603'''
DEFAULT_REQUEST_HEADERS = {
   #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, sdch',
    'accept-language':'zh-CN,zh;q=0.8',
   # 'cookie':'PHPSESSID=44efmbfrmlc2f6i4c6opdkfvb6; __unam=d0030f5-15a72aef977-69e8404-71; _ga=GA1.3.1126361205.1491027434',
   # 'Cookie':'__jsluid=1b796f21ead6721b307e3a1e3b8546eb; csrftoken=ALBTZXkIAKvHDkyCped07HXitAi3tFCC; __jsl_clearance=1492069343.596|0|zFNtbX1laPHKAlQ4lpCayk7SrAI%3D; Hm_lvt_6b15558d6e6f640af728f65c4a5bf687=1491035454,1491270738,1492069349; Hm_lpvt_6b15558d6e6f640af728f65c4a5bf687=1492069671',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Connection':'keep-alive'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'oday.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'oday.middlewares.RandomUserAgent': 543,
   # 'oday.middlewares.ProxyMiddleware': 542,
    'oday.middlewares.SeleniumMiddleware':543,
   #  'scrapy.downloadermiddlewares.retry.RetryMiddleware':200,
}
RETRY_TIMES = 0
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408,502]

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'oday.pipelines.OdayPipeline': 300,
    'oday.pipelines.MySQLPipeline':400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
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

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

PROXIES = [
    {'ip_port': '106.46.136.139:808', 'user_pass': ''},
    {'ip_port': '123.207.143.51:8080', 'user_pass': ''},
    {'ip_port': '121.40.42.35:9999', 'user_pass': ''},
    {'ip_port': '115.29.2.139:80', 'user_pass': ''},
    {'ip_port': '124.88.67.16:80', 'user_pass': ''},
    {'ip_port': '221.216.94.77:808', 'user_pass': ''},
    {'ip_port': '222.187.227.40:10000', 'user_pass': ''},
    {'ip_port': '182.148.114.171:3128', 'user_pass': ''},
    {'ip_port': '202.202.90.20:8080', 'user_pass': ''},
]

DOWNLOAD_DELAY=3

COMMANDS_MODULE = 'oday.commands'
COOKIES_ENABLED= True
#COOKIE_DEBUG = True

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

SELENIUM_TIMEOUT = 120
CHROME_EXECUTALE_PATH='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver'
