
from django.conf.urls import url, include
from django.contrib import admin

from chapter import views

urlpatterns = [
    url('chapter/', views.chapter, name='chapter'),

]
