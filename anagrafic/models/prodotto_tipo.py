from django.db import models


class ProdottoType(models.Model):
    name = models.CharField(max_length=200)
    gas = models.ForeignKey("Gas", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "gas")
