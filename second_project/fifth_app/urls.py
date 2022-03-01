from django.conf.urls import url
from fifth_app import views

# TEMPLATE TAGGING 
app_name = 'fifth_app'


urlpatterns = [ 
    url(r'^other/$', views.other, name='other'),
    url(r'^base/$', views.base, name='base'),
    url(r'^index/$', views.index, name='index'),
]