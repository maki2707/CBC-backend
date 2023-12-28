from rest_framework import serializers
from .models import GlavniLik

class GlavniLikSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlavniLik
        fields = '__all__'