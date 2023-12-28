from django.db import models
from django.conf import settings

class GlavniLik(models.Model):
    idGlavniLik = models.AutoField(primary_key=True)
    nazivGlavniLik = models.CharField(max_length=30)
    opisGlavniLik = models.CharField(max_length=500)

    def __str__(self):
        return self.nazivGlavniLik



class Strip(models.Model):
    idStrip = models.AutoField(primary_key=True)
    godinaIzdanja = models.IntegerField()
    broj = models.IntegerField()
    nazivStrip = models.CharField(max_length=50)
    idGlavniLik = models.ForeignKey(GlavniLik, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazivStrip
    
