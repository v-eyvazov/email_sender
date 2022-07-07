from djongo import models


# Create your models here.

class Email(models.Model):
    _id = models.ObjectIdField()
    email_to = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    sent_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.subject} at {self.sent_date}"
