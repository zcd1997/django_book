from celery import task, shared_task

from userhelper import send_mail_to

@shared_task
def send_mail_celery(username,  active_url, receive_mail, title):
    #send_mail("Test", "Hello", settings.EMAIL_HOST_USER, [email])
    send_mail_to(username,  active_url, receive_mail, title)