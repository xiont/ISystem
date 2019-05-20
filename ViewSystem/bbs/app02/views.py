#encoding=utf-8
from __future__ import division
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.shortcuts import render,render_to_response,HttpResponseRedirect,HttpResponse
import models
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.conf import settings
from app01 import  models as models1
from bbs import classify_5
from django.db.models import Q
import re
# Create your views here.
def secret(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        this_user = models1.BBS_user.objects.get(user__username = request.user)
        return render_to_response( 'secret.html',{'this_user':this_user,'request':request})
        #return render(request, 'secret.html', {'secret_list':secret_list})

def visual(request):
    this_user = models1.BBS_user.objects.get(user__username = request.user)
    return render_to_response( 'visual.html',{'this_user':this_user,'request':request})


def showphoto(request,EID):
    # if EID == 'oday_pie':
    #     numlist30 = returnnumlist(30)
    #     numlist60 = returnnumlist(60)
    #     numlist90 = returnnumlist(90)
    #     print numlist30
    #     return render(request, ""+EID+'.html',{'numlist30':numlist30,
    #                                        'numlist60':numlist60,
    #                                        'numlist90':numlist90})
    #
    # elif EID == 'oday_line':
    #     otherlist,buglist,datalist = returnnumlist_change(20)
    #     return render(request, ""+EID+'.html',{ 'otherlist':otherlist,
    #                                        'buglist':buglist,
    #                                        'datalist':datalist})
    # else:
    pass

def showissue(request,IID):
    if IID == 'bug360':
        secret_list = models.Oday.objects.all().order_by('-time')

        page = request.GET.get('page','1')
        paginator = JuncheePaginator(secret_list, 17)
        try:
            secrets = paginator.page(int(page))
        except PageNotAnInteger:
            secrets = paginator.page(9)
        except EmptyPage:
            secrets = paginator.page(paginator.num_pages)
        return render(request, 'oday_issue.html', {'secret_list':secrets})
    elif IID == 'oday_issue':
        bug360_list = models.Bobao360.objects.all().order_by('-time')
        page = request.GET.get('page', 1)

        paginator = JuncheePaginator(bug360_list,20)
        try:
            bug360_lists = paginator.page(page)
        except PageNotAnInteger:
            bug360_lists = paginator.page(9)
        except EmptyPage:
            bug360_lists = paginator.page(paginator.num_pages)
        return render(request, 'bug360.html', {'bug360_list':bug360_lists})
    else:
        pass

def show_event(request):
    this_user = models1.BBS_user.objects.get(user__username = request.user)
    eventlists = models.Security_event.objects.all().order_by('-event_time')
    page = request.GET.get('page','1')
    search =  request.GET.get('search','')
    if search:
        eventlists = models.Security_event.objects.filter(Q(event_platform__icontains=search)|Q(event_title__icontains=search)).order_by('-event_time')
    else:
        pass

    paginator = JuncheePaginator(eventlists, 10)
    try:
        eventlist = paginator.page(int(page))
    except PageNotAnInteger:
        eventlist = paginator.page(9)
    except EmptyPage:
        eventlist = paginator.page(paginator.num_pages)
    return render(request,'event.html',{'this_user':this_user,'eventlist':eventlist,'search':search})

def show_bug(request):
    this_user = models1.BBS_user.objects.get(user__username = request.user)
    buglists = models.Bug.objects.all().order_by('-bug_time')
    page = request.GET.get('page','1')
    bugname = request.GET.get('bugname','');bugid = request.GET.get('bugid','');bugplatform = request.GET.get('bugplatform','')
    search =  request.GET.get('search','')
    if search:
        buglists = buglists.filter(Q(bug_name__icontains=search)|Q(bug_id__icontains=search)|Q(bug_platform__icontains=search)).order_by('-bug_time')
    if not bugname:
        buglists = buglists.filter(Q(bug_id__icontains=search)|Q(bug_platform__icontains=search)).order_by('-bug_time')
    if not bugid:
        buglists = buglists.filter(Q(bug_name__icontains=search)|Q(bug_platform__icontains=search)).order_by('-bug_time')
    if not bugplatform:
        buglists = buglists.filter(Q(bug_id__icontains=search)|Q(bug_name__icontains=search)).order_by('-bug_time')
    paginator = JuncheePaginator(buglists, 10)
    try:
        buglist = paginator.page(int(page))
    except PageNotAnInteger:
        buglist = paginator.page(9)
    except EmptyPage:
        buglist = paginator.page(paginator.num_pages)
    return render(request,'bug.html',{'this_user':this_user,'buglist':buglist,'search':search,'bugname':bugname,'bugid':bugid,'bugplatform':bugplatform})


def superview(request):
    # now = datetime.datetime.now()
    # timedelta = datetime.timedelta(days=1)
    # day2 = now - timedelta;day3 = day2 - timedelta;day4 = day3 -timedelta;day5 = day4 -timedelta;day6 = day5 -timedelta;day7 = day6 - timedelta
    #
    # events = models.Security_event.objects.all()
    # list1 = events.filter(event_time = now);list2 = events.filter(event_time = day2);list3 = events.filter(event_time = day3)
    # list4 = events.filter(event_time = day4);list5 = events.filter(event_time = day5);list6 = events.filter(event_time = day6);list7 = events.filter(event_time = day7)
    # event_num = [list1.count(),list2.count(),list3.count(),list4.count(),list5.count(),list6.count(),list7.count()]
    # recent_event = events.order_by("-event_time")[0:4]
    #
    # bugs = models.Bug.objects.all()
    # blist1 = bugs.filter(bug_time = now);blist2 = bugs.filter(bug_time = day2);blist3 = bugs.filter(bug_time = day3)
    # blist4 = bugs.filter(bug_time = day4);blist5 = bugs.filter(bug_time = day5);blist6 = bugs.filter(bug_time = day6);blist7 = bugs.filter(bug_time = day7)
    # bug_num = [blist1.count(),blist2.count(),blist3.count(),blist4.count(),blist5.count(),blist6.count(),blist7.count()]
    # recent_bug = bugs.order_by("-bug_time")[0:4]
    #
    # recent_7event = events.filter(event_time__gte = day7)
    # eventtype_num = {'other':0,'badpgm':0,'intattack':0,'information':0,'equipment':0}
    # for item in recent_7event:
    #     if lastClassify(str(item.event_title).replace('	','').replace('\n','').lstrip().rstrip()) == 1:
    #         eventtype_num['other'] +=1
    #     if lastClassify(str(item.event_title).replace('	','').replace('\n','').lstrip().rstrip()) == 2:
    #         eventtype_num['badpgm'] +=1
    #     if lastClassify(str(item.event_title).replace('	','').replace('\n','').lstrip().rstrip()) == 3:
    #         eventtype_num['intattack'] +=1
    #     if lastClassify(str(item.event_title).replace('	','').replace('\n','').lstrip().rstrip()) == 4:
    #         eventtype_num['information'] +=1
    #     if lastClassify(str(item.event_title).replace('	','').replace('\n','').lstrip().rstrip()) == 5:
    #         eventtype_num['equipment'] +=1
    # total = float(eventtype_num['badpgm']+eventtype_num['intattack']+eventtype_num['information']+eventtype_num['equipment'])
    # percentage = [format(float(eventtype_num['badpgm'])/total, '.2%'),format(float(eventtype_num['intattack'])/total, '.2%'),format(float(eventtype_num['information'])/total, '.2%'),format(float(eventtype_num['equipment'])/total, '.2%')]
    #
    #
    # recent_7bugs = models.Bug.objects.filter(bug_time__gte = day7)
    # bugs_total = recent_7bugs.count()
    # CNVD_count = recent_7bugs.filter(bug_platform ='CNVD').count()
    # CNNVD_count = recent_7bugs.filter(bug_platform ='CNNVD').count()
    # Seebug_count = recent_7bugs.filter(bug_platform ='Seebug').count()
    # Exploite_count = recent_7bugs.filter(bug_platform = 'Exploit').count()
    # count_360 = bugs_total - CNVD_count -CNNVD_count-Seebug_count-Exploite_count
    # bug7_list=[CNVD_count,CNNVD_count,Seebug_count,Exploite_count,count_360,0,0]
    # return render(request,'superview.html',{
    #     'event_num':event_num,
    #     'bug_num':bug_num,
    #     'recent_event':recent_event,
    #     'recent_bug':recent_bug,
    #     'eventtype_num':eventtype_num,
    #     'percentage':percentage,
    #     'bug7_list':bug7_list,
    # })

    pass

import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def SSRview(request,TP):
    colors = ['#a5c2d5','#cbab4f','#76a871','#a56f8f','#c12c44','#a56f8f','#9f7961','#76a871','#6f83a5']
    if TP=='1':#漏洞类型数量统计 Webapps Local&Privilege Remote 拒绝服务&PoC 移动互联网漏洞 电信行业漏洞 操作系统漏洞 应用程序漏洞 网络设备漏洞
        bugs = models.Bug.objects.all()
        count1 = bugs.filter(bug_type = 'Webapps').count()+bugs.filter(bug_type = '移动互联网漏洞').count()#WebApps
        count2 = bugs.filter(bug_type = 'Local&Privilege').count() #Local&Privilege
        count3 = bugs.filter(bug_type = 'Remote').count()#Remote
        count4 = bugs.filter(bug_type = '拒绝服务&PoC').count()#拒绝服务&PoC
        count5 = bugs.filter(bug_type = '电信行业漏洞').count()#电信行业漏洞
        count6 = bugs.filter(bug_type = '操作系统漏洞').count()#操作系统漏洞
        count7 = bugs.filter(bug_type = '应用程序漏洞').count()#应用程序漏洞
        count8 = bugs.filter(bug_type = '网络设备漏洞').count()#网络设备漏洞
        title = "各类型漏洞统计"
        data = [
            {'name' : 'WebApps','value' : count1,'color':'#a5c2d5'},
		   	{'name' : 'Local&Privilege','value' : count2,'color':'#cbab4f'},
		   	{'name' :  'Remote','value' :count3,'color':'#76a871'},
		   	{'name' :'拒绝服务&PoC','value' : count4,'color':'#76a871'},
		   	{'name' :'电信行业漏洞','value' : count5,'color':'#a56f8f'},
		   	{'name' :'操作系统漏洞','value' : count6,'color':'#c12c44'},
		   	{'name' :'应用程序漏洞','value' : count7,'color':'#a56f8f'},
		   	{'name' :'网络设备漏洞','value' : count8,'color':'#9f7961'},
        ]
        dict = {"title":title,"data":data}
        return HttpResponse(json.dumps(dict))
    if TP=='2':
        KeyStr = request.POST['KeyStr']
        title = "威胁信息关键词统计"
        bugs = models.Bug.objects.all()
        events = models.Security_event.objects.all()
        keywords = KeyStr.split(";")
        data=[]
        for i in range(0,len(keywords)):
            data.append({'name':keywords[i],'value':bugs.filter(Q(bug_name__icontains=keywords[i])).count()+events.filter(Q(event_title__icontains=keywords[i])).count(),'color':colors[i]})
        # count1 = bugs.filter(Q(bug_name__icontains='Windows')).count()
        # count2 = bugs.filter(Q(bug_name__icontains='Linux')).count()
        # count3 = bugs.filter(Q(bug_name__icontains='Mysql')).count()
        # count4 = bugs.filter(Q(bug_name__icontains='Microsoft')).count() Windows;Linux;MySQL;Microsoft;php;Oracle;Apple;Apache
        # count5 = bugs.filter(Q(bug_name__icontains='php')).count()
        # count6 = bugs.filter(Q(bug_name__icontains='Oracle')).count()
        # count7 = bugs.filter(Q(bug_name__icontains='Apple')).count()
        # count8 = bugs.filter(Q(bug_name__icontains='Apache')).count()
        # xNum = [count1,count2,count3,count4,count5,count6,count7,count8]
        # print xNum
        dict = {"title":title,"data":data}
        print dict
        return HttpResponse(json.dumps(dict))
    if TP=='3':
        title="7天安全事件数量统计"
        now = datetime.datetime.now()
        timedelta = datetime.timedelta(days=1)
        day2 = now - timedelta;day3 = day2 - timedelta;day4 = day3 -timedelta;day5 = day4 -timedelta;day6 = day5 -timedelta;day7 = day6 - timedelta

        events = models.Security_event.objects.all()
        list1 = events.filter(event_time = now);list2 = events.filter(event_time = day2);list3 = events.filter(event_time = day3)
        list4 = events.filter(event_time = day4);list5 = events.filter(event_time = day5);list6 = events.filter(event_time = day6);list7 = events.filter(event_time = day7)
        event_num = [list1.count(),list2.count(),list3.count(),list4.count(),list5.count(),list6.count(),list7.count()]
        recent_event = events.order_by("-event_time")[0:4]
        #lables=
        dict = {
            'value':event_num,
            'labels':['今天','昨天','前两天','前三天','前四天','前五天','前六天'],
            'title':title
        }
        return HttpResponse(json.dumps(dict))
    if TP=='4':
        title ="7天安全漏洞数量统计"
        bugs = models.Bug.objects.all()
        now = datetime.datetime.now()
        timedelta = datetime.timedelta(days=1)
        day2 = now - timedelta;day3 = day2 - timedelta;day4 = day3 -timedelta;day5 = day4 -timedelta;day6 = day5 -timedelta;day7 = day6 - timedelta
        blist1 = bugs.filter(bug_time = now);blist2 = bugs.filter(bug_time = day2);blist3 = bugs.filter(bug_time = day3)
        blist4 = bugs.filter(bug_time = day4);blist5 = bugs.filter(bug_time = day5);blist6 = bugs.filter(bug_time = day6);blist7 = bugs.filter(bug_time = day7)
        bug_num = [blist1.count(),blist2.count(),blist3.count(),blist4.count(),blist5.count(),blist6.count(),blist7.count()]
        lables=['今天','昨天','前两天','前三天','前四天','前五天','前六天']
        dict = {
            'value':bug_num,
            'labels':lables,
            'title':title
        }
        return HttpResponse(json.dumps(dict))
    if TP=='5':
        title = "近期安全事件分类情况分析"
        now = datetime.datetime.now()
        timedelta = datetime.timedelta(days=1)
        day2 = now - timedelta;day3 = day2 - timedelta;day4 = day3 -timedelta;day5 = day4 -timedelta;day6 = day5 -timedelta;day7 = day6 - timedelta
        events = models.Security_event.objects.all()
        recent_7event = events.filter(event_time__gte = day7)
        eventtype_num = {'other':0,'badpgm':0,'intattack':0,'information':0,'equipment':0}
        for item in recent_7event:
            if lastClassify(str(item.event_title).replace('	','').replace('\n','').lstrip().rstrip()) == 1:
                eventtype_num['other'] +=1
            if lastClassify(str(item.event_title).replace('	','').replace('\n','').lstrip().rstrip()) == 2:
                eventtype_num['badpgm'] +=1
            if lastClassify(str(item.event_title).replace('	','').replace('\n','').lstrip().rstrip()) == 3:
                eventtype_num['intattack'] +=1
            if lastClassify(str(item.event_title).replace('	','').replace('\n','').lstrip().rstrip()) == 4:
                eventtype_num['information'] +=1
            if lastClassify(str(item.event_title).replace('	','').replace('\n','').lstrip().rstrip()) == 5:
                eventtype_num['equipment'] +=1
        data = [
			        {'name' : '网络有害程序','value' : eventtype_num['badpgm'],'color':'#a5c2d5'},
			        {'name' : '网络威胁攻击','value' : eventtype_num['intattack'],'color':'#cbab4f'},
			        {'name' : '信息威胁相关','value' : eventtype_num['information'],'color':'#76a871'},
			        {'name' : '网络安全设备','value' : eventtype_num['equipment'],'color':'#9f7961'}]
        dict={'title':title,'data':data}
        return HttpResponse(json.dumps(dict))
    if TP=='6':
        title = "漏洞发布平台统计"
        now = datetime.datetime.now()
        timedelta = datetime.timedelta(days=1)
        day2 = now - timedelta;day3 = day2 - timedelta;day4 = day3 -timedelta;day5 = day4 -timedelta;day6 = day5 -timedelta;day7 = day6 - timedelta
        recent_7bugs = models.Bug.objects.filter(bug_time__gte = day7)
        bugs_total = recent_7bugs.count()
        CNVD_count = recent_7bugs.filter(bug_platform ='CNVD').count()
        CNNVD_count = recent_7bugs.filter(bug_platform ='CNNVD').count()
        Seebug_count = recent_7bugs.filter(bug_platform ='Seebug').count()
        Exploite_count = recent_7bugs.filter(bug_platform = 'Exploit').count()
        count_360 = bugs_total - CNVD_count -CNNVD_count-Seebug_count-Exploite_count
        data = [
			        	{'name' : 'CNVD','value' : CNVD_count,'color':'#fedd74'},
			        	{'name' : 'CNNVD','value' : CNNVD_count,'color':'#82d8ef'},
			        	{'name' : 'Seebug','value' : Seebug_count,'color':'#f76864'},
			        	{'name' : 'Exploit','value' : Exploite_count,'color':'#80bd91'},
			        	{'name' : '360播报','value' : count_360,'color':'#fd9fc1'}
		        	]
        dict={'title':title,'data':data}
        return HttpResponse(json.dumps(dict))
    if TP=="7":
        InTime = request.POST["InTime"]
        ToTime = request.POST["ToTime"]
        title = "按照时间间隔为"+InTime+"天,总时间为"+ToTime+"天的漏洞数量统计"
        now = datetime.datetime.now()
        timedelta = datetime.timedelta(days=int(InTime))
        ttimedelta = datetime.timedelta(days=int(ToTime))
        Xtimes=[]
        it = now
        while it >= (now-ttimedelta):
            Xtimes.append(it)
            it = it - timedelta
        Xdata=[]
        bugs = models.Bug.objects.all()
        for i in range(0,len(Xtimes)-1):
            co = bugs.filter(bug_time__lte = Xtimes[i]).filter(bug_time__gte = Xtimes[i+1]).count()
            Xdata.append(co)

        Xlabels = []
        for i in range(len(Xtimes)-1):
            Xlabels.append(Xtimes[i].strftime("%Y-%m-%d")+"\n至\n"+Xtimes[i+1].strftime("%Y-%m-%d"))
        print Xlabels
        print Xdata
        data=[]
        for i in range(0,len(Xlabels)):
            data.append({"name":Xlabels[i],"value":Xdata[i],"color":"#97b3bc"})
        dict={'title':title,'data':data}
        return HttpResponse(json.dumps(dict))
    if TP=="8":
        InTime = request.POST["InTime"]
        ToTime = request.POST["ToTime"]
        EventKey = request.POST["EventKey"]
        title = "按照时间间隔为"+InTime+"天,总时间为"+ToTime+"天的"+EventKey+"关键词统计"
        now = datetime.datetime.now()
        timedelta = datetime.timedelta(days=int(InTime))
        ttimedelta = datetime.timedelta(days=int(ToTime))
        Xtimes=[]
        it = now
        while it >= (now-ttimedelta):
            Xtimes.append(it)
            it = it - timedelta
        Xdata=[]
        bugs = models.Bug.objects.all()
        events = models.Security_event.objects.all()
        for i in range(0,len(Xtimes)-1):
            co = bugs.filter(bug_time__lte = Xtimes[i]).filter(bug_time__gte = Xtimes[i+1]).filter(Q(bug_name__icontains=EventKey )).count()
            co2 = events.filter(event_time__lte = Xtimes[i]).filter(event_time__gte = Xtimes[i+1]).filter(Q(event_title__icontains=EventKey )).count()
            Xdata.append(co+co2)
        Xlabels = []
        for i in range(len(Xtimes)-1):
            Xlabels.append(Xtimes[i].strftime("%Y-%m-%d")+"\n至\n"+Xtimes[i+1].strftime("%Y-%m-%d"))
        print Xlabels
        print Xdata
        data=[]
        for i in range(0,len(Xlabels)):
            data.append({"name":Xlabels[i],"value":Xdata[i],"color":"#97b3bc"})
        dict={'title':title,'data':data}
        return HttpResponse(json.dumps(dict))
    if TP=="main":
        this_user = models1.BBS_user.objects.get(user__username = request.user)
        now = datetime.datetime.now()
        timedelta = datetime.timedelta(days=1)
        day2 = now - timedelta;day3 = day2 - timedelta;day4 = day3 -timedelta;day5 = day4 -timedelta;day6 = day5 -timedelta;day7 = day6 - timedelta

        events = models.Security_event.objects.all()
        recent_event = events.order_by("-event_time")[0:10]

        bugs = models.Bug.objects.all()
        recent_bug = bugs.order_by("-bug_time")[0:10]
        return render(request,'ssrview.html',{'this_user':this_user,'recent_event':recent_event,'recent_bug':recent_bug})

from  docs import User as MongoUser
from docs import Event_Mongo
def Mongo(request):
    events = models.Security_event.objects.all().order_by("-event_time")[0:100]
    for each in events:
        try:
            event = Event_Mongo(title = each.event_title,time = each.event_time,url = each.event_url,platform = each.event_platform)
            event.save()
        except:
            pass
    list = []
    for item in Event_Mongo.objects:
        print item['title'],item['time'],item['id']
        list.append(Event_Mongo.to_json(item))
    return HttpResponse(list)




#####################################################################################
from bbs.settings import SITE_CAB,SITE_CLASSES,SITE_FULLTEXT,MY_VOCABLIST
from bbs import classify_5

def lastClassify(teststring):
    listClasses = SITE_CLASSES
    myVocabList = MY_VOCABLIST
    trainMat = []
    for postinDoc in SITE_CAB:
        trainMat.append(classify_5.setOfWords2Vec(myVocabList,postinDoc))

    p1,p2,p3,p4,p5,pab,pbb,pcb,pdb,peb = classify_5.trainNB0(trainMat,listClasses)
    '''print p0
    print p1
    print p2
    print pab,pbb'''
    testlist = classify_5.parse_str_to_list(teststring)
    thisDoc = classify_5.bagOfWords2VecMN(myVocabList,testlist)
    return classify_5.classifyNB(thisDoc,p1,p2,p3,p4,p5,pab,pbb,pcb,pdb,peb)



#fen ye chu li dai ma
class JuncheePaginator(Paginator):
    def __init__(self, object_list, per_page, range_num=5, orphans=0, allow_empty_first_page=True):
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
        self.range_num = range_num

    def page(self, number):
        self.page_num = number
        return super(JuncheePaginator, self).page(number)

    def _page_range_ext(self):
        num_count = 2 * self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages + 1)
        num_list = []
        num_list.append(self.page_num)
        for i in range(1, self.range_num + 1):
            if self.page_num - i <= 0:
                num_list.append(num_count + self.page_num - i)
            else:
                num_list.append(self.page_num - i)

            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + i)
            else:
                num_list.append(self.page_num + i - num_count)
        num_list.sort()
        return num_list
    page_range_ext = property(_page_range_ext)



