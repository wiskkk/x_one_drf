from celery import shared_task
from django.core.mail import send_mail

from users.models import MyUser
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def everyday_send_email():
    """
    Задача для отправки статистики по электронной почте.
    """
    users = MyUser.objects.all()
    mails = []
    for user in users:
        subject = f'Statistic for user - {user}'
        message = f'Dear {user}, your amount for today morning is {user.amount}'
        mails.append(send_mail(subject,
                               message,
                               'artiom95moskvin@gmail.com',
                               [user.email],
                               fail_silently=False))
    return mails
