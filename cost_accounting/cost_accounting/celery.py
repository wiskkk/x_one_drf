import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cost_accounting.settings')

app = Celery('cost_accounting', broker="redis://redis:6379/0")

app.config_from_object('django.conf:settings')
app.conf.beat_schedule = {
    'Send_mail_to_User': {
        'task': 'management.tasks.everyday_send_email',
        'schedule': crontab(hour=6),  # every 6AM seconds it will be called
    }
}
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
