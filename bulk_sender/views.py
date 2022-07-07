from django.core.mail import BadHeaderError
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST

from bulk_sender.send_for_types.send import *
from bulk_sender.serializers import EmailSerializer
from bulk_sender.reciever_types import Receiver

# Create your views here.

receivers = {
    Receiver.ALL: send_to_all,
    Receiver.THREE_MONTHS: send_to_last_three_months,
    Receiver.SIX_MONTHS: send_to_last_six_months,
}


@api_view(["POST"])
def send_email(request):
    try:
        email_to = request.data["emailTo"]
        subject = request.data["subject"]
        message = request.data["message"]
    except KeyError:
        return Response({"status": "forbidden",
                         "message": "Invalid request."},
                        status=HTTP_400_BAD_REQUEST)

    if email_to and subject and message:
        try:
            receiver = Receiver[email_to]
            send = receivers[receiver]
            return send(subject=subject, message=message)
        except (BadHeaderError, KeyError):
            return Response({"status": "forbidden",
                             "message": "Invalid header found."},
                            status=HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({"status": "failed",
                         "message": "Make sure all fields are entered and valid."},
                        status=HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def get_email_history(request):
    emails = Email.objects.using("mongodb").all()
    serialized_emails = EmailSerializer(emails, many=True)
    return Response(serialized_emails.data)
