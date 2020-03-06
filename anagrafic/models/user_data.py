from django.contrib.auth.models import User
from django.db import models

class UserData(models.Model):
    gas = models.ForeignKey("Gas", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=15, null=True, blank=True)
    codice_fiscale= models.CharField(max_length=20, null=True, blank=True)
    adress = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.gas} {self.user.get_full_name()}"