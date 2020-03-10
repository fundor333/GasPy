from django.db import models


class Fornitore(models.Model):
    name = models.ForeignKey(max_length=200)
    gas = models.ForeignKey("Gas", on_delete=models.CASCADE)
    prodotto = models.ForeignKey("ProdottoType", on_delete=models.CASCADE)
    certificato_produttore = models.ForeignKey(max_length=200,null=True, blank=True)
    sito = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "gas")
