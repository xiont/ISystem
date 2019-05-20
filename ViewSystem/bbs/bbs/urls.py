"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from logReg import views as logview
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login,{'template_name':"login.html"}),
    url(r'^regist/$',logview.register),
     url(r'^regist/captcha/$', logview.captcha),
    url(r'^index/$', logview.index),
    url(r'^logout/$',logout,{'template_name':"index.html"}),
    url(r'^changepassword/(?P<username>\w+)/$',logview.changepassword),
    url(r'^usersetting/(?P<user_id>\d+)/',logview.usersetting),
    url(r'',include('app01.urls')),
    url(r'',include('app02.urls')),
]+static( settings.STATIC_URL , document_root = settings.STATIC_ROOT)
