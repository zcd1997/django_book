
from django.conf.urls import url, include
from django.contrib import admin

from search import views

urlpatterns = [
    url('search/', views.search, name='search'),

]
