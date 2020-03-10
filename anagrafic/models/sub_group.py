from django.db import models


class SubGroup(models.Model):
    name = models.CharField(max_length=200)
    gas = models.ForeignKey("GAS", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.gas.name} - {self.name}"

    class Meta:
        unique_together =("name", "gas")