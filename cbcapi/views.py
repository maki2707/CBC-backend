from django.shortcuts import render

from rest_framework import viewsets
from .models import GlavniLik
from .serializers import GlavniLikSerializer

class GlavniLikViewSet(viewsets.ModelViewSet):
    queryset = GlavniLik.objects.all()
    serializer_class = GlavniLikSerializer


def get_queryset(self):
    queryset = GlavniLik.objects.all()
    search_term = self.request.query_params.get('searchTerm', None)
    if search_term is not None:
        queryset = queryset.filter(nazivGlavniLik__icontains=search_term)
    return queryset
