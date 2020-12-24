from django.conf.urls import url
from . import views



urlpatterns = [
    
    url(r'^$' , views.home , name='home'),
    url(r'^about/$' , views.about , name='about'),
    url(r'^contact_us/$' , views.contact_us , name='contact_us'),
    url(r'^panel/$' , views.panel , name='panel'),
    url(r'^login/$' , views.my_login , name='my_login'),
    url(r'^logout/$' , views.my_logout , name='my_logout'),
    url(r'^panel/setting/$' , views.site_setting , name='site_setting'),
    url(r'^panel/about/setting/$' , views.about_setting , name='about_setting'),
    url(r'^panel/change/pass/$' , views.change_pass , name='change_pass'),
    url(r'^registration/$' , views.my_registration , name='my_registration'),
    url(r'^answer/comments/(?P<pk>\d+)/$' , views.answer_cm , name='answer_cm'),
    url(r'^show/data/$' , views.show_data , name='show_data'),
]
