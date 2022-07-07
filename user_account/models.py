from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField()
    last_login = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} ({self.last_login})"
