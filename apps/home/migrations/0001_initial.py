# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-13 22:30
from __future__ import unicode_literals

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='小说ID')),
                ('book_img', models.CharField(max_length=255, verbose_name='小说图片')),
                ('book_title', models.CharField(max_length=255, verbose_name='小说名称')),
                ('book_introduce', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='小说简介')),
                ('book_state', models.CharField(max_length=64, verbose_name='小说状态')),
                ('book_author', models.CharField(max_length=64, verbose_name='小说作者')),
                ('book_price', models.DecimalField(decimal_places=2, default=10.0, max_digits=7, verbose_name='折扣价')),
                ('book_stock', models.IntegerField(default=10, verbose_name='库存')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '小说管理',
                'verbose_name_plural': '小说管理',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='分类ID')),
                ('cate_list_url', models.CharField(max_length=500, verbose_name='分类地址')),
                ('cate_list_text', models.CharField(max_length=64, unique=True, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '小说分类',
                'verbose_name_plural': '小说分类',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('ch_id', models.AutoField(primary_key=True, serialize=False, verbose_name='章节ID')),
                ('ch_name', models.CharField(max_length=255, verbose_name='章节名')),
                ('ch_url', models.CharField(max_length=255, verbose_name='章节链接')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('book', models.ForeignKey(db_column='book_id', on_delete=django.db.models.deletion.DO_NOTHING, to='home.Book', verbose_name='书籍管理')),
            ],
            options={
                'verbose_name': '章节管理',
                'verbose_name_plural': '章节管理',
                'db_table': 'chapter',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False, verbose_name='订单ID')),
                ('order_code', models.CharField(max_length=255, verbose_name='订单号')),
                ('address', models.CharField(max_length=255, verbose_name='配送地址')),
                ('post', models.CharField(max_length=255, verbose_name='邮编')),
                ('receiver', models.CharField(max_length=255, verbose_name='收货人')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('user_message', models.CharField(max_length=255, verbose_name='附加信息')),
                ('create_date', models.DateTimeField(max_length=0, verbose_name='创建日期')),
                ('pay_date', models.DateTimeField(blank=True, max_length=0, null=True, verbose_name='支付时间')),
                ('confirm_date', models.DateTimeField(blank=True, null=True, verbose_name='确认日期')),
                ('status', models.IntegerField(choices=[(1, '正常'), (2, '未支付'), (0, '异常'), (-1, '删除')], default=1, verbose_name='订单状态')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单管理',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False, verbose_name='购物车ID')),
                ('number', models.IntegerField(default=0, verbose_name='小说数量')),
                ('status', models.IntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Book', verbose_name='小说ID')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'shop_car',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户地址ID')),
                ('user_name', models.CharField(max_length=500, verbose_name='用户姓名')),
                ('address_p', models.CharField(max_length=500, verbose_name='地区地址')),
                ('address_r', models.CharField(max_length=500, verbose_name='详细地址')),
                ('postcode', models.CharField(max_length=500, verbose_name='邮编')),
                ('phone', models.CharField(max_length=100, verbose_name='电话')),
            ],
            options={
                'verbose_name': '用户地址管理',
                'verbose_name_plural': '用户地址管理',
                'db_table': 'useraddress',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('phone', models.CharField(default='110', max_length=11, verbose_name='用户电话')),
                ('desc', DjangoUeditor.models.UEditorField(default='', verbose_name='用户简介')),
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'db_table': 'user_profile',
            },
        ),
        migrations.AddField(
            model_name='useraddress',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='home.UserProfile', verbose_name='用户ID'),
        ),
        migrations.AddField(
            model_name='shopcar',
            name='user_id',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='home.UserProfile', verbose_name='用户ID'),
        ),
        migrations.AddField(
            model_name='order',
            name='car_id',
            field=models.ForeignKey(db_column='car_id', on_delete=django.db.models.deletion.DO_NOTHING, to='home.ShopCar', verbose_name='购物车ID'),
        ),
        migrations.AddField(
            model_name='order',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='home.UserProfile', verbose_name='用户ID'),
        ),
        migrations.AddField(
            model_name='book',
            name='cate',
            field=models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.DO_NOTHING, to='home.Category', verbose_name='书籍分类'),
        ),
    ]