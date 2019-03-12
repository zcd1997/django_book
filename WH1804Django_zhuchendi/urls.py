from django.conf.urls import url, include
from django.contrib import admin
import xadmin
from home import views

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('^ueditor/', include('DjangoUeditor.urls')),
    url('^$', views.index),
    url('home/', include('home.urls')),
    url('user/', include('user.urls')),
    url('book_detail/', include('book_detail.urls')),
    url('search/', include('search.urls')),
    url('chapter/', include('chapter.urls')),
    url('category/', include('categorys.urls')),
    url('car/', include('car.urls')),
    url('order/', include('order.urls')),
    url('pay/', include('pay.urls')),
]
