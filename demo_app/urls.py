from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('data',views.name_data,name='data'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    
    ]