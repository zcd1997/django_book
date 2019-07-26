from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import defaults

from user.context_processors import shop_count
from home.models import *
from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt
def add(request):
    # 判断是否是ajax请求
    if request.is_ajax():
        if request.user.is_authenticated():
            try:
                """
                参数  商品的数量
                参数  商品的id
                """
                with transaction.atomic():
                    uid = request.user.id
                    book_id = request.POST.get('book_id')
                    number = request.POST.get('number')
                    """
                    当商品已经存在用户的购物车的时候,更新数量
                    当商品不存在用户的购物车的时候 创建该记录
                   """
                    cars = ShopCar.objects.filter(user_id=uid, book_id=book_id, status=1)
                    if cars:
                        car = cars.first()
                        #     表示存在就去更新
                        car.number = F('number') + number
                        # car.number += number
                        car.save(update_fields=['number'])
                    else:
                        car = ShopCar(user_id_id=uid, book_id=book_id, number=number)
                        car.save()
                        # 正常情况下返回json数据
                    data = shop_count(request)
                    data['status'] = 200
                    data['msg'] = 'success'
                    return JsonResponse(data=data)
            except Exception as e:
                # 表示添加购物车失败
                return JsonResponse(data={'status': 404, 'msg': 'error'})
        else:
            #  表示没有登录
            return redirect('/user/login/')
    else:
        return HttpResponse('错误的请求')


@csrf_exempt
def delete(request):
    try:
        car_id = request.POST.get('car_id')
        car = ShopCar.objects.get(car_id=car_id, status=1)
        car.status = -1
        car.save(update_fields=['status'])
        data = shop_count(request)
        data['status'] = 200
        data['msg'] = 'success'
        return JsonResponse(data=data)
    except:
        return JsonResponse({'status': 404, 'msg': 'error'})


# # 吐司
@csrf_exempt
def update_num(request):
    try:
        ac = request.POST.get('ac')
        car_id = request.POST.get('car_id')
        if ac == '1':
            count = ShopCar.objects.filter(car_id=car_id, status=1).update(number=F('number') + 1)
        else:
            # count = ShopCar.objects.filter(car_id=car_id, status=1).update(number=F('number') - 1)
            cars = ShopCar.objects.filter(car_id=car_id, status=1)
            car = cars.first().number
            if car > 1:
                count = cars.update(number=F('number') - 1)
        data = shop_count(request)
        data['status'] = 200
        data['msg'] = 'success'
        return JsonResponse(data=data)
    except Exception as e:
        return JsonResponse({'status': 404, 'msg': 'error'})


#
#
# # 减的操作
#
#
@csrf_exempt
def list(request):
    if request.user.is_authenticated():
        cars = ShopCar.objects.filter(user_id=request.user.userprofile.uid, status=1)
        return render(request, 'car.html', {'cars': cars})
    else:
        return redirect('/user/login/')
