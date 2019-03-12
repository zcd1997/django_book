from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class UserProfile(models.Model):
    phone = models.CharField(verbose_name='用户电话', max_length=11, default='110')
    desc = UEditorField(verbose_name="用户简介", width=1000, height=600,
                        imagePath="arts_ups/ueditor/", filePath="arts_ups/ueditor/",
                        toolbars="full", default='')
    uid = models.AutoField(verbose_name='用户ID', primary_key=True)
    user = models.OneToOneField('auth.User')

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name


class UserAddress(models.Model):
    address_id = models.AutoField(verbose_name='用户地址ID', primary_key=True)
    user_name = models.CharField(verbose_name='用户姓名', max_length=500)
    address_p = models.CharField(verbose_name='地区地址', max_length=500)
    address_r = models.CharField(verbose_name='详细地址', max_length=500)
    postcode = models.CharField(verbose_name='邮编', max_length=500)
    phone = models.CharField(verbose_name="电话", max_length=100)
    uid = models.ForeignKey(UserProfile, models.DO_NOTHING, db_column='uid', verbose_name="用户ID")

    class Meta:
        db_table = 'useraddress'
        verbose_name = '用户地址管理'
        verbose_name_plural = '用户地址管理'


class Category(models.Model):
    cate_id = models.CharField(verbose_name='分类ID', max_length=64, primary_key=True)
    cate_list_url = models.CharField(verbose_name='分类地址', max_length=500)
    cate_list_text = models.CharField(verbose_name='分类名称', max_length=64, unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = '小说分类'
        verbose_name_plural = '小说分类'


class Book(models.Model):
    book_id = models.CharField(verbose_name='小说ID', max_length=64, primary_key=True)
    book_img = models.CharField(verbose_name='小说图片', max_length=255)
    book_title = models.CharField(verbose_name='小说名称', max_length=255)
    book_introduce = UEditorField(verbose_name="小说简介", width=1000, height=600,
							 imagePath="arts_ups/ueditor/", filePath="arts_ups/ueditor/",
							 blank=True, toolbars="full", default='')
    book_state = models.CharField(verbose_name='小说状态', max_length=64)
    book_author = models.CharField(verbose_name='小说作者', max_length=64)
    book_price = models.DecimalField(verbose_name='折扣价', max_digits=7, decimal_places=2, default=10.00)
    book_stock = models.IntegerField(verbose_name='库存', default=10)
    cate = models.ForeignKey(Category, models.DO_NOTHING, db_column='cate_id', db_index=True, verbose_name='书籍分类')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'book'
        verbose_name = '小说管理'
        verbose_name_plural = verbose_name


class Chapter(models.Model):
    ch_id = models.AutoField(verbose_name='章节ID', primary_key=True)
    ch_name = models.CharField(verbose_name='章节名', max_length=255)
    ch_url = models.CharField(verbose_name='章节链接', max_length=255)
    book = models.ForeignKey(Book, models.DO_NOTHING, db_column='book_id', db_index=True, verbose_name='书籍管理')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'chapter'
        verbose_name = '章节管理'
        verbose_name_plural = verbose_name





class ShopCar(models.Model):
    car_id = models.AutoField(verbose_name='购物车ID', primary_key=True)
    number = models.IntegerField(verbose_name='小说数量', default=0)
    book = models.ForeignKey(Book, models.DO_NOTHING, verbose_name='小说ID')
    user_id = models.ForeignKey(UserProfile, models.DO_NOTHING, db_column='uid', verbose_name='用户ID')
    # 1正常 -1 删除 ， 禁止 2
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'shop_car'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

class Order(models.Model):
    ORDER_STATUS = (
        (1, '正常'),
        (2, '未支付'),
        (0, '异常'),
        (-1, '删除'),
    )

    oid = models.AutoField('订单ID', primary_key=True)
    # 订单号唯一
    order_code = models.CharField('订单号', max_length=255)
    address = models.CharField('配送地址', max_length=255)
    post = models.CharField('邮编', max_length=255)
    receiver = models.CharField('收货人', max_length=255)
    mobile = models.CharField('手机号', max_length=11)
    user_message = models.CharField('附加信息', max_length=255)
    create_date = models.DateTimeField('创建日期', max_length=0)
    pay_date = models.DateTimeField('支付时间', max_length=0,
                                    blank=True, null=True)
    confirm_date = models.DateTimeField('确认日期', blank=True, null=True)
    """ 1正常 0 异常, -1 删除 """
    status = models.IntegerField('订单状态', choices=ORDER_STATUS, default=1)
    uid = models.ForeignKey(UserProfile, models.DO_NOTHING, db_column='uid', verbose_name="用户ID")
    car_id = models.ForeignKey(ShopCar,models.DO_NOTHING,db_column='car_id',verbose_name='购物车ID')

    def __str__(self):
        return self.order_code

    class Meta:
        db_table = 'order'
        verbose_name = '订单'
        verbose_name_plural = '订单管理'