
from django.conf.urls import url, include
from django.contrib import admin

from pay import views

urlpatterns = [
    url('pay_money/',views.paymoney,name='pay_money')
]
