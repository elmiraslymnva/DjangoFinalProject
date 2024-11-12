from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Django'nun ayarlarını kullanarak Celery'yi ayarla
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoFinalProject.settings')

app = Celery('DjangoFinalProject')

# Celery için broker'ı RabbitMQ olarak ayarla
app.conf.broker_url = 'amqp://guest:guest@rabbitmq:5672//'

# Celery ayarlarını yükle, settings.py içindeki CELERY_* ayarları burada kullanılacak
app.config_from_object('django.conf:settings', namespace='CELERY')

# Django'daki task'ları otomatik olarak bul ve kaydet
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    """
    Debug amaçlı kullanılan bir task. Task çalışma isteği hakkında bilgi verir.
    """
    print('Request: {0!r}'.format(self.request))



