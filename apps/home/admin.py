from django.contrib import admin

# Register your models here.
from home.models import *
import xadmin
from xadmin import views


class BaseStyleSettings:
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseStyleSettings)


class GlobalSettings:
    site_title = '图书后台管理系统'
    site_footer = 'Python1804有限公司'
    menu_style = 'accordion'  # 后台菜单样式修改


xadmin.site.register(views.CommAdminView, GlobalSettings)


class UserProfileAdmin:
    list_display = ['phone', 'desc', 'uid']
    search_fields = ['phone', 'desc', 'uid']
    style_fields = {'desc': 'ueditor'}

xadmin.site.register(UserProfile, UserProfileAdmin)


class UserAddressAdmin:
    list_display = ['address_id', 'user_name', 'address_p', 'address_r', 'postcode', 'phone', 'uid']
    search_fields = ['address_id', 'user_name', 'address_p', 'address_r', 'postcode', 'phone', 'uid']


xadmin.site.register(UserAddress, UserAddressAdmin)


class CategoryAdmin:
    list_display = ['cate_id', 'cate_list_url', 'cate_list_text']
    search_fields = ['cate_id', 'cate_list_url', 'cate_list_text']


xadmin.site.register(Category, CategoryAdmin)


class BookAdmin:
    list_display = ['book_id', 'book_img', 'book_title', 'book_introduce', 'book_state', 'book_author', 'book_price',
                    'book_stock', 'cate', 'create_date']
    search_fields = ['book_id', 'book_img', 'book_title', 'book_introduce', 'book_state', 'book_author', 'book_price',
                     'book_stock', 'cate', 'create_date']
    style_fields = {'book_introduce': 'ueditor'}

xadmin.site.register(Book, BookAdmin)


class ChapterAdmin:
    list_display = ['ch_id', 'ch_name', 'ch_url', 'book', 'create_date']
    search_fields = ['ch_id', 'ch_name', 'ch_url', 'book', 'create_date']


xadmin.site.register(Chapter, ChapterAdmin)


class OrderAdmin:
    list_display = ['oid', 'order_code', 'address', 'post', 'receiver'
        , 'mobile', 'user_message', 'create_date', 'pay_date',
                    'confirm_date', 'status',
                    'uid']
    search_fields = ['oid', 'order_code', 'address', 'post', 'receiver'
        , 'mobile', 'user_message', 'create_date', 'pay_date',
                     'confirm_date', 'status',
                     'uid']


xadmin.site.register(Order, OrderAdmin)


class ShopCarAdmin:
    list_display = ['car_id', 'number', 'book', 'user_id']
    search_fields = ['car_id', 'number', 'book', 'user_id']


xadmin.site.register(ShopCar, ShopCarAdmin)
