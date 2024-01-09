from rest_framework import serializers
from .models import GlavniLik, ListaZelja, Strip,Kolekcija

class GlavniLikSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlavniLik
        fields = '__all__'

class StripSerializer(serializers.ModelSerializer):
    inCollection = serializers.SerializerMethodField()

    class Meta:
        model = Strip
        fields = ['idStrip', 'godinaIzdanja', 'broj', 'nazivStrip', 'idGlavniLik', 'inCollection']

    def get_inCollection(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, "user") and request.user.is_authenticated:
            return Kolekcija.objects.filter(idKorisnik=request.user, idStrip=obj).exists()
        return False

class KolekcijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kolekcija
        fields = '__all__'

class ListaZeljaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaZelja
        fields = '__all__'        