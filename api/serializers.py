from rest_framework import serializers
from .models import GlavniLik, Strip

class GlavniLikSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlavniLik
        fields = '__all__'

class StripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strip
        fields = '__all__'

