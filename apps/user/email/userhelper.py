from django.core.mail import send_mail
from django.template import loader

from WH1804Django_zhuchendi import settings

def send_mail_to(username,  active_url, receive_mail, title="xxx"):
    '''
    active_url： 用户点击激活URL，可以出发用户的状态
    :param username:
    :param active_url:
    :param receive_mail:
    :param title:
    :return:
    '''
    subject = "欢迎使用我们的系统-邮件激活"

    temp = loader.get_template('user_active.html')

    data = {
        "username": username,
        "active_url": active_url
    }

    html_message = temp.render(context=data)

    send_mail(subject, title, from_email=settings.EMAIL_HOST_USER, recipient_list=[receive_mail],
              html_message=html_message)


# def get_user_by_id(id):
#     try:
#         user = User.objects.get(pk=id)
#         return user
#     except:
#         return None
