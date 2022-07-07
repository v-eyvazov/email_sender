from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from datetime import datetime, timedelta

from bulk_sender.reciever_types import Receiver
from user_account.models import User
from bulk_sender.models import Email


def send_to_all(subject, message):
    users = list(User.objects.filter(is_active__in=[True]).values_list("email", flat=True))  # noqa
    if users:  # noqa
        send_mail(subject=subject,
                  message=message,
                  from_email=None,
                  recipient_list=users,
                  fail_silently=False)
        email = Email(email_to=Receiver.ALL, subject=subject, message=message)
        email.save(using="mongodb")
        return Response({"status": "success"})
    else:
        return Response({"status": "failed",
                         "message": "No users found."},
                        status=HTTP_500_INTERNAL_SERVER_ERROR)


def send_to_last_three_months(subject, message):
    last_three_month = datetime.today() - timedelta(days=90)
    users = list(User.objects.filter(last_login__gte=last_three_month,  # noqa
                                     is_active__in=[True]).values_list("email", flat=True))  # noqa
    if users:  # noqa
        send_mail(subject=subject,
                  message=message,
                  from_email=None,
                  recipient_list=users,
                  fail_silently=False)
        email = Email(email_to=Receiver.THREE_MONTHS, subject=subject, message=message)
        email.save(using="mongodb")
        return Response({"status": "success"})
    else:
        return Response({"status": "failed",
                         "message": "No users found."},
                        status=HTTP_500_INTERNAL_SERVER_ERROR)


def send_to_last_six_months(subject, message):
    last_six_months = datetime.today() - timedelta(days=180)
    users = list(User.objects.filter(last_login__gte=last_six_months,  # noqa
                                     is_active__in=[True]).values_list("email", flat=True))  # noqa
    if users:  # noqa
        send_mail(subject=subject,
                  message=message,
                  from_email=None,
                  recipient_list=users,
                  fail_silently=False)
        email = Email(email_to=Receiver.SIX_MONTHS, subject=subject, message=message)
        email.save(using="mongodb")
        return Response({"status": "success"})
    else:
        return Response({"status": "failed",
                         "message": "No users found."},
                        status=HTTP_500_INTERNAL_SERVER_ERROR)
