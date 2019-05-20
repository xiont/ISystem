#encoding:utf-8

from django.template import RequestContext
from app01 import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User
from app01.models import BBS_user
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response,render
from django.utils.http import (base36_to_int, is_safe_url,
                               urlsafe_base64_decode, urlsafe_base64_encode)
import os
from django.contrib import auth
from logReg.forms import LoginForm

from logReg.forms import RegisterForm
from logReg.forms import ChangepwdForm
from logReg.forms import User_settingForm
from django.contrib.sites.models import SiteManager
import json
import base64
import logging
def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html',RequestContext(request,{'form':form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return render(request,'index.html',RequestContext(request))
            else:
                return render(request,'login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render(request,'login.html',RequestContext(request,{'form':form,}))

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/index/",RequestContext(request))

"""
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            auth.login(request, new_user)
            return render_to_response("index.html",{'user':request.user})
    else:
        form = UserCreationForm()
    return render_to_response("regist.html", {
        'form': form,
    },RequestContext(request))
"""

def register(request):
    error=[]
    print "OK-------------------"
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            password = data['password']
            password2= data['password2']
            captcha = data['captcha']
            if not captcha==request.session['captcha']:
                error.append('请输入正确的验证码')
            elif not request.COOKIES.get('is_yanzhen','')=='is':
                error.append('请滑动验证条')
            else:
                if not User.objects.all().filter(username=username):
                    if form.pwd_validate(password, password2):
                        user = User.objects.create_user(username, email, password)
                        user.save()
                        #BBS_user.objects.all().filter(id=user.id).update(user__username=username)
                        auth.login(request, user)
                        this_user = models.BBS_user.objects.get(user__username = request.user)
                        response = render(request,'index.html',{'this_user':this_user})
                        response.delete_cookie('is_yanzhen',path='/regist')
                        return response
                    else:
                        error.append('Please input the same password')
                else:
                    error.append('The username has existed,please change your username')
    else:
        form = RegisterForm()
    response = render(request,'register.html',{'form':form,'error':error})
    response.delete_cookie('is_yanzhen',path='/regist')
    return response

def index(request):
    bbs_list = models.BBS.objects.all().order_by("-id")
    list = []
    for i in range(len(bbs_list)):
        set = {'image':BBS_user.objects.get(user__username =bbs_list[i].author ).photo,'title':bbs_list[i].title,'summary':bbs_list[i].summary,'time':bbs_list[i].created_at,'sign':bbs_list[i].sign,'id':bbs_list[i].id,
               'author':bbs_list[i].author}
        list.append(set)
    try:
        this_user = models.BBS_user.objects.get(user__username = request.user)
    except:
        this_user = request.user
    #for i in range(len(bbs_list)):

    return render(request, 'index.html', {'bbs_list':list,'this_user':this_user})

def changepassword(request,username):
    if request.user.is_authenticated():
        error = []
        this_user = models.BBS_user.objects.get(user__username = request.user)
        if request.method == 'POST':
            form = ChangepwdForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = auth.authenticate(username=username,password=data['old_pwd'])
                if user is not None:
                    if data['new_pwd']==data['new_pwd2']:
                        newuser = User.objects.get(username__exact=username)
                        newuser.set_password(data['new_pwd'])
                        newuser.save()
                        return render(request,'login.html')
                    else:
                        error.append('Please input the same password')
                else:
                    error.append('Please correct the old password')
            else:
                error.append('Please input the required domain')
        else:
            form = ChangepwdForm()
        return render(request,'changepassword.html',{'form':form,'error':error,'this_user':this_user,'request':request})
    else:
        return HttpResponseRedirect('/index/')

def usersetting(request,user_id):
    if request.method == "POST":
        form = User_settingForm(request.POST,request.FILES)
        print form
        if form.is_valid():
            f = request.FILES.get('photo')
            baseDir = os.path.dirname(os.path.abspath(__name__))
            jpgdir = os.path.join(baseDir,'static','images')
            def file_extension(path):
                return os.path.splitext(path)[1]
            str = file_extension(f.name)
            filename = os.path.join(jpgdir,request.user.username+'.GIF')
            fobj = open(filename,'wb')
            for chrunk in f.chunks():
                fobj.write(chrunk)
            fobj.close()
            imge = Image.open(filename)
            imge.thumbnail((45, 45), Image.ANTIALIAS)
            imge.save(filename,'GIF')
            #os.remove(filename)
            photo = 'static/images/%s'%(request.user.username+'.GIF')
            BBS_user.objects.filter(id = user_id).update(photo = photo)
            #BBS_user.save()
            print photo
            this_user = models.BBS_user.objects.get(user__username = request.user)
            return render(request,'usersetting.html',{'this_user':this_user,'request':request})
        else:
            this_user = models.BBS_user.objects.get(user__username = request.user)
            return render(request,'usersetting.html',{'this_user':this_user,'request':request})
    else:
        form = User_settingForm()
    this_user = models.BBS_user.objects.get(user__username = request.user)
    return render(request,'usersetting.html',{'this_user':this_user,'request':request})


from PIL import Image, ImageDraw, ImageFont, ImageFilter
from django.http.response import HttpResponse
import cStringIO, string, os, random







def captcha(request):
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    '''Captcha'''
    #image = Image.new('RGB', (147, 49), color = (255, 255, 255)) # model, size, background color
    image,rand_str = create_validate_code()
    #font_file = os.path.join(BASE_DIR, 'static/fonts/Arial.ttf') # choose a font file
    #font = ImageFont.truetype(font_file, 47) # the font object
    draw = ImageDraw.Draw(image)
    #rand_str = ''.join(random.sample(string.letters + string.digits, 4)) # The random string
    #draw.text((7, 0), rand_str, fill=(0, 0, 0), font=font) # position, content, color, font
    del draw
    request.session['captcha'] = rand_str.lower() # store the content in Django's session store
    buf = cStringIO.StringIO() # a memory buffer used to store the generated image
    image.save(buf, 'jpeg')
    return HttpResponse(buf.getvalue(), 'image/jpeg') # return the image data stream as image/jpeg format, browser will treat it as an image


####################################验证码生成#############################################
_letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper()  # 大写字母
_numbers = ''.join(map(str, range(3, 10)))  # 数字
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def create_validate_code(size=(140, 30),
                         chars=init_chars,
                         img_type="GIF",
                         mode="RGB",
                         bg_color=(255, 255, 255),
                         fg_color=(0, 0, 255),
                         font_size=18,
                         font_type=os.path.join(BASE_DIR, 'static/fonts/Arial.ttf') ,# choose a font file
                         length= 6,
                         draw_lines=True,
                         n_line=(3, 4),
                         draw_points=True,
                         point_chance = 2):
    '''
    @todo: 生成验证码图片
    @param size: 图片的大小，格式（宽，高），默认为(120, 30)
    @param chars: 允许的字符集合，格式字符串
    @param img_type: 图片保存的格式，默认为GIF，可选的为GIF，JPEG，TIFF，PNG
    @param mode: 图片模式，默认为RGB
    @param bg_color: 背景颜色，默认为白色
    @param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
    @param font_size: 验证码字体大小
    @param font_type: 验证码字体，默认为 ae_AlArabiya.ttf
    @param length: 验证码字符个数
    @param draw_lines: 是否划干扰线
    @param n_lines: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
    @param draw_points: 是否画干扰点
    @param point_chance: 干扰点出现的概率，大小范围[0, 100]
    @return: [0]: PIL Image实例
    @return: [1]: 验证码图片中的字符串
    '''

    width, height = size # 宽， 高
    img = Image.new(mode, size, bg_color) # 创建图形
    draw = ImageDraw.Draw(img) # 创建画笔

    def get_chars():
        '''生成给定长度的字符串，返回列表格式'''
        return random.sample(chars, length)

    def create_lines():
        '''绘制干扰线'''
        line_num = random.randint(*n_line) # 干扰线条数
        for i in range(line_num):
            # 起始点
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            #结束点
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        '''绘制干扰点'''
        chance = min(100, max(0, int(point_chance))) # 大小限制在[0, 100]
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))
    def create_strs():
        '''绘制验证码字符'''
        c_chars = get_chars()
        strs = ' %s ' % ' '.join(c_chars) # 每个字符前后以空格隔开
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)
        draw.text(((width - font_width) / 3, (height - font_height) / 3),
                    strs, font=font, fill=fg_color)

        return ''.join(c_chars)
    if draw_lines:
        create_lines()
    if draw_points:
        create_points()
    strs = create_strs()
    # 图形扭曲参数
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    img = img.transform(size, Image.PERSPECTIVE, params) # 创建扭曲
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) # 滤镜，边界加强（阈值更大）
    return img, strs

