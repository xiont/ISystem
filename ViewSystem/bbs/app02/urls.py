__author__ = 'Administrator'
from django.conf.urls import url
import views
urlpatterns = [
    url(r'secret_issue/$',views.secret),
    url(r'visual/$',views.visual),
    url(r'visual/(?P<EID>\w+)/$',views.showphoto),
    url(r'visual/issues/(?P<IID>\w+)/$',views.showissue),
    url(r'event/$',views.show_event),
    url(r'bug/$',views.show_bug),
    url(r'mongo/$',views.Mongo),
    url(r'superview/$',views.superview),
    url(r'ssrview/$',views.SSRview),
    url(r'ssrview/(?P<TP>\w+)/$',views.SSRview),
]
