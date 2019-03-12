import datetime
import random

from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from home.models import Order, ShopCar, UserAddress
from user.context_processors import shop_count


@csrf_exempt
def confirm(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            try:
                car_id_list = request.POST.get('car_id')
                car_ids = car_id_list.split(',')
                for i in range(len(car_ids)):
                    car = ShopCar.objects.get(car_id=car_ids[i], status=1)
                    car.status = -1
                    car.save(update_fields=['status'])
                request.session['car_ids'] = car_ids
                # for i in range(len(car_ids)):
                #     car_id = car_ids[i]
                # order_code = random.randint(0, 999999)
                # create_time = datetime.datetime.now(tz=datetime.timezone.utc)
                data = shop_count(request)
                data['status'] = 200
                data['msg'] = 'success'
                return JsonResponse(data=data)

            except Exception as e:
                # 表示添加订单失败
                data = shop_count(request)
                data['status'] = 400
                data['msg'] = 'error'
                return JsonResponse(data=data)
        else:
            car_ids = request.session['car_ids']
            for i in range(len(car_ids)):
                car_id = car_ids[i]
                order_code = random.randint(0, 99999999)
                create_date = datetime.datetime.now()
                order = Order(order_code=order_code, create_date=create_date, status=2, uid_id=request.user.id,
                              car_id_id=car_id)
                order.save()
            car_id = ShopCar.objects.filter(car_id__in=car_ids)
            addresses = UserAddress.objects.filter(uid=request.user.id)
            return render(request, 'order.html', {'car_id': car_id, 'addresses': addresses})
    else:
        return redirect('/user/login/')


@csrf_exempt
def add_address(request):
    if request.method == "POST":
        address_p = request.POST.get('address_p')
        address_r = request.POST.get('address_r')
        postcode = request.POST.get('postcode')
        user_name = request.POST.get('user_name')
        phone = request.POST.get('phone')

        add = UserAddress(address_p=address_p, address_r=address_r, postcode=postcode, user_name=user_name,
                          phone=phone,
                          uid_id=request.user.id)
        add.save()
        car_ids = request.session['car_ids']
        car_id = ShopCar.objects.filter(car_id__in=car_ids)
        addresses = UserAddress.objects.filter(uid=request.user.id)
        return render(request, 'order.html', {'car_id': car_id, 'addresses': addresses})


@csrf_exempt
def showorder(request):
    if request.user.is_authenticated():

        orders = Order.objects.filter(uid_id=request.user.id)
        return render(request,'order_list.html',{'orders':orders})
    else:
        return redirect('/user/login/')