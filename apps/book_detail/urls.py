
from django.conf.urls import url, include
from django.contrib import admin

from book_detail import views

urlpatterns = [
    url('detail/', views.detail, name='detail'),

]
