from django.urls import path

from confirmation import views

urlpatterns = [
    path("confirmation/", views.confirmation_sender),
    path("confirm/<str:encrypted_email>", views.confirmation_receiver),
]
