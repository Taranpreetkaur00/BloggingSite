from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog_detail/(?P<word>.*)/$' , views.blog_detail , name='blog_detail'),
    url(r'^panel/blog/list/$' , views.blog_list , name='blog_list'), 
    url(r'^panel/blog/add/$' , views.blog_add , name='blog_add'),  
    url(r'^panel/blog/del/(?P<pk>\d+)/$' , views.blog_delete , name='blog_delete'),
    url(r'^panel/blog/edit/(?P<pk>\d+)/$' , views.blog_edit , name='blog_edit'),
    url(r'^panel/blog/publish/(?P<pk>\d+)/$' , views.blog_publish , name='blog_publish'),
    url(r'^urls/(?P<pk>\d+)/$' , views.blog_detail_short , name='blog_detail_short'),
    url(r'^blog/all/(?P<word>.*)/$' , views.blog_all_show , name='blog_all_show'),
    url(r'^all/blog/$' , views.all_blog , name='all_blog'), 
     url(r'^all/blog/search/$' , views.all_blog_search , name='all_blog_search'), 
]