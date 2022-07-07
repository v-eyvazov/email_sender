from rest_framework import serializers
from bulk_sender.models import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ("_id", "email_to", "subject", "message", "sent_date",)
