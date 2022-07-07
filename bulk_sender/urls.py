from django.urls import path

from bulk_sender import views

urlpatterns = [
    path("send/", views.send_email),
    path("history/", views.get_email_history),
]
