from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnlie.settings import EMAIL_FROM
from MxOnline.celery import app


def random_str(randomlength=8):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

@app.task
def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        emial_title = '慕学在线网激活链接'
        email_body = '请点击下面链接激活账号：127.0.0.1：8000/active/{0}'.format(code)

        send_status = send_mail(emial_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
        else:
            print('错误')
    elif send_type == 'forget':
        emial_title = '慕学在线网密码重置链接'
        email_body = '请点击下面链接重置密码：127.0.0.1：8000/reset/{0}'.format(code)
        send_status = send_mail(emial_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'update_email':
        emial_title = '慕学在线网修改密码验证码'
        email_body = '你的邮箱验证码为：{0}'.format(code)
        send_status = send_mail(emial_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass