from alipay import AliPay
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from WH1804Django_zhuchendi import settings
from home.models import Order
from user.context_processors import shop_count


@csrf_exempt
def paymoney(request):
    if request.method == "POST":
        try:
            car_ids = request.session['car_ids']
            address_p = request.POST.get('address_p')
            address_r = request.POST.get('address_r')
            user_name = request.POST.get('user_name')
            phone = request.POST.get('phone')
            postcode = request.POST.get('postcode')
            sum_money = 0
            for i in range(len(car_ids)):
                order = Order.objects.get(car_id=car_ids[i])
                sum_money += (int(order.car_id.number) * int(order.car_id.book.book_price))
                # order.address_p = address_p
                order.address = address_p + address_r
                order.receiver = user_name
                order.mobile = phone
                order.post = postcode
                order.save()
            request.session['sum_money'] = sum_money
            data = shop_count(request)
            data['status'] = 200
            data['msg'] = 'success'
            return JsonResponse(data=data)
        except Exception as e:
            data = shop_count(request)
            data['status'] = 400
            data['msg'] = 'error'
            return JsonResponse(data=data)

    else:
        sum_money = request.session['sum_money']
        # 创建用于进行支付宝支付的工具对象
        alipay = AliPay(
            appid=settings.APP_ID,
            app_notify_url=None,  # 默认回调url
            app_private_key_string=settings.APP_PRIVATE_STRING,
            alipay_public_key_string=settings.ALIPAY_PUBLIC_KEY_STRING,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True  # 默认False  配合沙箱模式使用
        )
        # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
        order_string = alipay.api_alipay_trade_page_pay(
            # 订单号
            out_trade_no='123456',
            # 商品总价
            total_amount=str(sum_money),  # 将Decimal类型转换为字符串交给支付宝
            # 订单标题
            subject="图书商城-{}".format(123456),
            # 支付成功之后 前端跳转的界面
            return_url='https://127.0.0.1:8000/',
            # 支付成功后台跳转接口
            notify_url=None  # 可选, 不填则使用默认notify url
        )
        # 让用户进行支付的支付宝页面网址
        url = settings.ALI_PAY_URL + "?" + order_string
        del request.session['sum_money']
        del request.session['car_ids']
        return redirect(url)

######事务语句
#   with transaction.atomic:
