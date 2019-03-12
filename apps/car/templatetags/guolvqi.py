"""
过滤器:
    语法格式
    内置过滤器
    自定义过滤器
        1.创建一个 templatetags 的文件夹
        2.在该文件下新建一个py文件
        3.实例化注册器
        4.声明过滤器(过滤器的本质是一个函数)
        5.注册过滤器
        6.在模板中使用
            1.在需要自定义的过滤器的模板中 {% load  custom_filter %}
"""
from django import template

# 实例化注册 (固定格式)
register = template.Library()


@register.filter
def cheng(value, params):
    return value * params
