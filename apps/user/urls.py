
from django.conf.urls import url, include
from django.contrib import admin

from user import views

urlpatterns = [
    url('login/', views.login_view, name='login'),
    url('logout/', views.logout_view, name='logout'),
    url('register/', views.register, name='register'),
    url('active/',views.ActivateHandler,name='active')
]
