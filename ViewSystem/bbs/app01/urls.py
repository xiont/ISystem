__author__ = 'Administrator'
from django.conf.urls import url
import views
from django.conf import settings
from django.conf.urls.static import static
from logReg import views as lviews

urlpatterns = [
    url(r'^$',lviews.index),
    url(r'detail/(?P<bbs_id>\d+)/$',views.bbs_detail),
    url(r'detail/(?P<bbs_id>\d+)/sub_comment/$',views.sub_comment),
    url(r'sub_bbs/$',views.sub_bbs),
    #url(r'pub_bbs/$',views.pub_bbs),
]
