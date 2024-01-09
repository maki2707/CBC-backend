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
    
class Kolekcija(models.Model):
    idKolekcija = models.AutoField(primary_key=True)
    datumDodavanja = models.DateField(auto_now_add=True)  # Automatically set the date when the object is created
    idKorisnik = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    idStrip = models.ForeignKey('Strip', on_delete=models.CASCADE)

class ListaZelja(models.Model):
    idListaZelja = models.AutoField(primary_key=True)
    idStrip = models.ForeignKey(Strip, on_delete=models.CASCADE)
    idKorisnik = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('idStrip', 'idKorisnik')

    def __str__(self):
        return f"Wishlist {self.idListaZelja}"