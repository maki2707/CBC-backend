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


from rest_framework import serializers
from .models import StatusOglasa, Stanje, Oglas

class StatusOglasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOglasa
        fields = '__all__'

class StanjeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanje
        fields = '__all__'


from rest_framework import serializers
from .models import Oglas, Strip

class OglasSerializer(serializers.ModelSerializer):
    nazivStanje = serializers.CharField(source='idStanje.nazivStanja', read_only=True)
    nazivStatus = serializers.CharField(source='idStatus.nazivStatus', read_only=True)
    # Add new fields to fetch data from the Strip model
    nazivStrip = serializers.CharField(source='idStrip.nazivStrip', read_only=True)
    broj = serializers.IntegerField(source='idStrip.broj', read_only=True)
    godinaIzdanja = serializers.IntegerField(source='idStrip.godinaIzdanja', read_only=True)

    class Meta:
        model = Oglas
        fields = ['idOglas', 'datumObjave', 'cijena', 'idStrip', 'idKorisnik', 'idStatus', 'idStanje', 
                  'nazivStanje', 'nazivStatus', 'nazivStrip', 'broj', 'godinaIzdanja']
        extra_kwargs = {
            'idOglas': {'read_only': True},
            'datumObjave': {'read_only': True}
        }
