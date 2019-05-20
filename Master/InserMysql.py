#encoding:utf-8
import redis
import datetime
import MySQLdb
import MySQLdb.cursors
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
r = redis.Redis(host="127.0.0.1",port=6379,db=0)
def bobao():
    str_ = str(r.lpop("item:bobao"))
    b =eval(str_)
    item={}
    item["title"]=b["title"]
    item['time']=b["time"]
    item["link"]=b["link"]
    item['source']=b["source"]
    insertMysqlBobao(item)

def event():
    str_ = str(r.lpop("item:event"))
    b =eval(str_)
    item={}
    item["event_title"]=b["event_title"]
    item['event_time']=b["event_time"]
    item["event_url"]=b["event_url"]
    item['event_platform']=b["event_platform"]
    insertMysqlEvent(item)

def bug():
    str_ = str(r.lpop("item:bug"))
    b =eval(str_)
    item={}
    item["bug_name"]=b["bug_name"]
    item['bug_id']=b['bug_id']
    item["bug_time"]=b["bug_time"]
    item['bug_url']=b['bug_url']
    item['bug_platform']=b['bug_platform']
    item['bug_type']=b['bug_type']
    insertMysqlBug(item)

def oday():
    str_ = str(r.lpop("item:oday"))
    b =eval(str_)
    item={}
    item["title"]=b["title"]
    item['time']=b["time"]
    item["link"]=b["link"]
    insertMysqlOday(item)

def insertMysqlOday(item):
    print item
    db = MySQLdb.connect("localhost","root","1234","apple2",charset='utf8')
    cursor = db.cursor()
    c = datetime.datetime.strptime(item['time'],"%Y年%m月%d日")
    sql = "insert ignore into app02_oday(title,time,link) VALUES ('%s','%s', '%s')" % (item["title"], c, item["link"])
    sql2 = "insert ignore into app02_security_event(event_title,event_time,event_url,event_platform) VALUES ('%s','%s', '%s','%s')" % (item["title"], c, item["link"],'oday银行')
    cursor.execute(sql)
    cursor.execute(sql2)
    db.commit()
    db.close()

def insertMysqlBobao(item):
    print item
    db = MySQLdb.connect("localhost","root","1234","apple2",charset='utf8')
    cursor = db.cursor()
    cursor.execute("insert ignore into app02_bobao360 (title,time,link,source) values (%s, %s, %s,%s) ",(item["title"], item['time'], item["link"],item['source']))
    cursor.execute("insert ignore into app02_bug (bug_name,bug_id,bug_time,bug_url,bug_platform,bug_type) values (%s, %s, %s,%s,%s,%s) ",(item["title"],'',item['time'], item["link"],item['source'],''))
    db.commit()
    db.close()

def insertMysqlEvent(item):
    print item
    db = MySQLdb.connect("localhost","root","1234","apple2",charset='utf8')
    cursor = db.cursor()
    cursor.execute("insert ignore into app02_security_event (event_title,event_time,event_url,event_platform) values (%s, %s, %s,%s) ",(item["event_title"], item['event_time'], item["event_url"],item['event_platform']))
    db.commit()
    db.close()

def insertMysqlBug(item):
    print item
    db = MySQLdb.connect("localhost","root","1234","apple2",charset='utf8')
    cursor = db.cursor()
    cursor.execute("insert ignore into app02_bug (bug_name,bug_id,bug_time,bug_url,bug_platform,bug_type) values (%s, %s, %s,%s,%s,%s) ",(item["bug_name"], item['bug_id'], item["bug_time"],item['bug_url'],item['bug_platform'],item['bug_type']))
    db.commit()
    db.close()


while True:
    while r.exists("item:bobao"):
        try:
            bobao()
        except:pass
    while r.exists("item:event"):
        try:
            event()
        except:pass
    while r.exists("item:oday"):
        try:
            oday()
        except:pass
    while r.exists("item:bug"):
        try:
            bug()
        except:pass
