#encoding:utf-8
import redis
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

def timer(n):
  '''''
  每n秒执行一次
  '''
  while True:
    print time.strftime('%Y-%m-%d %X',time.localtime())
    r = redis.Redis(host="127.0.0.1",port=6379,db=0)
    # r.lpush("spider:oday","http://www.0daybank.org/")
    # r.lpush("spider:bobao","http://bobao.360.cn/vul/index?type=all")
    # r.lpush("spider:bug","http://www.baidu.com/")
    r.lpush("spider:event","http://other.51cto.com/")
    time.sleep(n)


if __name__ == "__main__":
    timer(120)
