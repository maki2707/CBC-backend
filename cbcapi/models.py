from django.db import models


class GlavniLik(models.Model):
    idGlavniLik = models.AutoField(primary_key=True)
    nazivGlavniLik = models.CharField(max_length=30)
    opisGlavniLik = models.CharField(max_length=500)

    def __str__(self):
        return self.nazivGlavniLik
