from django.conf.urls import url 
from second_app import views

urlpatterns = [ 
    url(r'^$', views.help, name='help'),
    url(r'^help/', views.about, name='about'),
    url(r'^date/', views.current_datetime, name='current_datetime'),
    url(r'^images/', views.images, name='images'),
    url(r'^database/', views.data_acc, name='data_acc'),
    url(r'^users/', views.users, name='users'),


]