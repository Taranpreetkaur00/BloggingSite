from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^comment/add/blog/(?P<pk>\d+)/$' , views.blog_cm_add , name='blog_cm_add'),
    url(r'^comments/list/$' , views.comments_list , name='comments_list'),
    url(r'^comments/delete/(?P<pk>\d+)/$' , views.comments_del , name='comments_del'),
    url(r'^comments/confirm/(?P<pk>\d+)/$' , views.comments_confirm , name='comments_confirm'), 

]