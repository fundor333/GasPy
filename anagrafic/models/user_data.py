from django.contrib.auth.models import User
from django.db import models

class UserData(models.Model):
    gas = models.ForeignKey("Gas", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    