from django.conf.urls import url, include
from django.contrib import admin

from car import views

urlpatterns = [
    url('add/', views.add, name='car_add'),
    url('list', views.list, name='car_list'),
    url('delete/', views.delete, name='car_delete'),
    url('update/', views.update_num, name='car_update'),

]
