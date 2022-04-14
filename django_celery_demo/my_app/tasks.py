import string

from celery import shared_task
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from django_celery_demo.celery import celery_app


@shared_task()
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(10)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)


@celery_app.task(bind=True)
def send_notification(self):
    print("\n\n Hi am notification !")
    return 'Notification Sent!'
