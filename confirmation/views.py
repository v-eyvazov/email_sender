from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from confirmation.cipher import encrypt, decrypt

# Create your views here.
from rest_framework.status import HTTP_400_BAD_REQUEST

from user_account.models import User


@api_view(['POST'])
def confirmation_sender(request):
    try:
        email = request.data["email"]
    except KeyError:
        return Response({"status": "forbidden",
                         "message": "Invalid request."},
                        status=HTTP_400_BAD_REQUEST)

    encrypted_email = encrypt(email)

    send_mail(subject="Email Confirmation",
              message=f"http://localhost:8000/email/confirm/{encrypted_email}",
              from_email=None,
              recipient_list=email.split(),
              fail_silently=False)

    return Response({"status": "success", "message": "Email was sent."})


@api_view(['GET'])
def confirmation_receiver(request, encrypted_email):
    if encrypted_email:
        email = decrypt(encrypted_email)
        user = User.objects.get(email=email)
        user.is_active = True
        user.save()
        return Response({"status": "success", "message": "Your account was activated!"})
    else:
        return Response({"status": "forbidden",
                         "message": "Invalid request."},
                        status=HTTP_400_BAD_REQUEST)
