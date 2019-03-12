import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 把apps添加到
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eqtb&*@t37ol6&4#cqq=0vpcrb&=*da2-o)#!yuv5m1lo6bu4b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition


# 系统内置app
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# 第三方app
EXT_APPS = [
    # xadmin模块
    'xadmin',
    'crispy_forms',
    # #主题模块
    'reversion',
    # django-celery
    # 'djcelery',
    'DjangoUeditor'

]
# 自定义APP
MY_APPS = [
    # 首页
    'home',
    # 用户
    'user',
    # 详情
    'book_detail',
    # 搜索
    'search',
    # 分类
    'categorys',
    # 章节
    'chapter',
    # 购物车
    'car',
    # 订单
    'order',
    #支付
    'pay'
]

INSTALLED_APPS = SYS_APPS + EXT_APPS + MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WH1804Django_zhuchendi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'user.context_processors.shop_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'WH1804Django_zhuchendi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shucheng',
        'USER': 'root',
        'PASSWORD': '123456',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 配置静态资源目录
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),

)

# 配置多媒体资源目录
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

############### celery settings begin #############
'''
celery是分布式异步消息队列处理框架
以redis作为MQ数据存储和转发
'''
REDIS_DEPLOY_FLAG = "test"

REDIS_SERVICE={
    'test':('127.0.0.1', '6379'),
    'online':('192.168.58.67', '10379'),
}

CELERY_BROKER_URL = 'redis://%s:%s/1' % (REDIS_SERVICE[REDIS_DEPLOY_FLAG][0],
                                         REDIS_SERVICE[REDIS_DEPLOY_FLAG][1])

CELERY_ACCEPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_BACKEND = 'django-db'

#部署的django服务的IP和端口
DJANGO_SERVICE = ('127.0.0.1',8000)


CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s:%s/1" % (REDIS_SERVICE[REDIS_DEPLOY_FLAG][0],
                                         REDIS_SERVICE[REDIS_DEPLOY_FLAG][1]),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

############### celery settings end #############
################# email settings begin #################
EMAIL_HOST = 'smtp.163.com'

EMAIL_PORT = 465
EMAIL_USE_SSL = True

#此账号是测试账号，不要乱用
EMAIL_HOST_USER = "15225412949@163.com"

#邮箱的客户端授权密码
EMAIL_HOST_PASSWORD = "zcd1997"

################# email settings end ###################


#######################支付宝配置   start####################
#注册应用时支付宝生成 app_id
APP_ID = '2016092100564521'
#支付网关

ALI_PAY_URL = 'https://openapi.alipaydev.com/gateway.do'
#私匙
APP_PRIVATE_STRING = open(BASE_DIR + '/alipay/rsa_private_key.pem').read()

#公匙放到支付宝上
ALIPAY_PUBLIC_KEY_STRING = open(BASE_DIR + '/alipay/rsa_public_key.pem').read()

#######################支付宝配置   end####################