from django.conf.urls import url, include
from django.contrib import admin

from order import views

urlpatterns = [
    url('confirm/', views.confirm, name='confirm'),
    url('address/', views.add_address, name='address'),
    url('showorder/', views.showorder, name='showorder')

]
