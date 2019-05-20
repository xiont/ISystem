from django.shortcuts import render,render_to_response,HttpResponseRedirect,HttpResponse
import models
from django_comments.models import Comment
import datetime
from forms import BBSForm
from django.contrib import auth
from django.template import RequestContext

# Create your views here.

def bbs_detail(request,bbs_id):
    bbs = models.BBS.objects.get( id = bbs_id)
    try:
        this_user = models.BBS_user.objects.get(user__username = request.user)
        print "sssss"
    except:
        this_user = ''
    comment_lists=[]
    Comments = Comment.objects.filter(object_pk = bbs_id)
    for comment in Comments:
        comment_lists.append({'user':comment.user,'photo':models.BBS_user.objects.get(user__username = comment.user).photo,'submit_data':comment.submit_date,'comment':comment.comment})
    return render(request,'detail.html',{'bbs':bbs,'this_user': this_user,'comment_lists':comment_lists})

def sub_comment(request,bbs_id):
    try:
        user_comment = request.POST.get('comment')
        Comment.objects.create(
            object_pk = bbs_id,
            content_type_id = 8,
            site_id = 1,
            user = request.user,
            comment = user_comment,
            submit_date = datetime.datetime.now(),
        )
        this_user = models.BBS_user.objects.get(user__username = request.user)
        csrftoken = request.COOKIES.get('csrftoken','')
        print csrftoken
        return HttpResponseRedirect('/detail/%s'% bbs_id,{'this_user': this_user,'csrftoken':csrftoken})
    except ValueError:
         return HttpResponseRedirect('/detail/%s'% bbs_id)




def sub_bbs(request):
    error = []
    if request.user.is_authenticated():
        this_user = models.BBS_user.objects.get(user__username = request.user)
        if request.method == 'POST':
            form = BBSForm(request.POST)
            if form.is_valid():
                print form
                data = form.cleaned_data
                title = data['title']
                summary = data['summary']
                sign = data['sign']
                content = data['content']
                author = models.BBS_user.objects.get(user__username = request.user)
                view_count =1
                ranking =2
                print "OKOKOKOKOK"
                BBS = models.BBS.objects.create(title=title,summary=summary,sign=sign,content=content,author=author,view_count=view_count,ranking=ranking)
                BBS.save()
                return render(request,'index.html',{'this_user':this_user})
            else:
                return render(request,'pub_bbs.html',{'form':form,'this_user':this_user})
        else:
            form = BBSForm()
            print "come here"
            return render(request,'pub_bbs.html',{'form':form,'request':request,'this_user':this_user})
    else:
        return HttpResponseRedirect('/login/')







    # try:
    #     this_user = models.BBS_user.objects.get(user__username = request.user)
    #     print '==>',request.POST.get('content')
    #     #bbs_category = request.POST.get('bbs_category')
    #     author = models.BBS_user.objects.get(user__username = request.user)
    #     models.BBS.objects.create(
    #         title = request.POST.get('title'),
    #         summary = request.POST.get('summary'),
    #         sign = request.POST.get('sign'),
    #         content = request.POST.get('content'),
    #         author = author,
    #         view_count =1,
    #         ranking =2 ,
    #     )
    #     return render_to_response('index.html',{'this_user':this_user})
    # except:
    #     try:
    #         this_user = models.BBS_user.objects.get(user__username = request.user)
    #         return render_to_response('pub_bbs.html',{'this_user':this_user})
    #     except:
    #         return HttpResponseRedirect('/login/')
