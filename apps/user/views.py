import uuid

from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.core.cache import cache

# Create your views here.

# 登录
from home.models import UserProfile


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login_text.html')
    elif request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login_text.html', {'msg': '用户名或密码错误'})
        except Exception as e:
            return render(request, 'login_text.html', {'msg': '网络异常请重试'})
    else:
        return render(request, 'login_text.html', {'msg': '不支持的请求方式'})


# 登出
def logout_view(request):
    logout(request)
    return redirect('/')


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register_text.html')
    elif request.method == 'POST':

        try:
            with transaction.atomic():
                username = request.POST.get('username')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                password = request.POST.get('password')
                confirm_password = request.POST.get('password2')
                if password and username and password == confirm_password:
                    users = User.objects.filter(username=username)
                    if users:
                        return render(request, 'register_text.html', {'msg': '该用户已存在'})
                        # 注册账号已经存在
                    else:
                        user = User.objects.create_user(username=username, password=password, email=email, is_active=0)
                        user.save()
                        user1 = User.objects.get(username=username)
                        userprofile = UserProfile.objects.create(user_id=user1.id, phone=phone)
                        userprofile.save()
                        try:
                            # 生成token  时间 + ip + 随机数
                            # uuid
                            token = str(uuid.uuid4())

                            cache.set(token, user.id, timeout=2 * 60 * 60 * 24)

                            active_url = "http://%s:%s/user/active/?token=%s" % (settings.DJANGO_SERVICE[0],
                                                                                 settings.DJANGO_SERVICE[1],
                                                                                 token)
                            from user.email import tasks
                            tasks.send_mail_celery(username, active_url, email, "注册邮箱激活")
                            return render(request, 'register_text.html', {'msg': '邮件已发送,请激活'})
                        except Exception as e:
                            return render(request, 'register_text.html', {'msg': '邮件发送失败,请重试'})
                        # 保存成功之后跳转到首页

                else:
                    # 参数不符合要求
                    return render(request, 'register_text.html', {'msg': '参数不正确'})
        except Exception as e:
            return render(request, 'register_text.html', {'msg': '网络异常请重试'})
    else:
        return render(request, 'register_text.html', {'msg': '不支持的请求方式'})


def ActivateHandler(request):
    token = request.GET.get('token')
    user_id = cache.get(token)

    if user_id:
        cache.delete(token)
        user = User.objects.get(pk=user_id)
        user.is_active = 1
        user.save()
        return HttpResponse(f"用户{user.username} 激活成功")
    else:
        return HttpResponse("激活用户信息过期，请重新申请激活邮件")
