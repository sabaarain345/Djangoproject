from django.conf.urls import url
from fifth_app import views

# TEMPLATE TAGGING 
app_name = 'fifth_app'


urlpatterns = [ 
    url(r'^other/$', views.other, name='other'),
    url(r'^base/$', views.base, name='base'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='user_login'),
    # url(r'^logout/$', views.user_logout, name='user_logout'),
    # url(r'^special/$', views.special, name='special'),
]