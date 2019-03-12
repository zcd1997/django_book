
from django.conf.urls import url, include
from django.contrib import admin

from categorys import views

urlpatterns = [
    url('category/', views.category, name='category'),

]
