from django.conf.urls import url 
from third_app_form import views

urlpatterns = [ 
    url(r'^index/', views.index, name='index'),
    url(r'^form/', views.form_name_view, name='form_name_view'),

]