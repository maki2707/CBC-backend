from rest_framework import viewsets
from .models import GlavniLik, Strip
from .serializers import GlavniLikSerializer, StripSerializer
from rest_framework.pagination import PageNumberPagination

class StandardResultsPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

class StripViewSet(viewsets.ModelViewSet):
    queryset = Strip.objects.all()
    serializer_class = StripSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        character_id = self.request.query_params.get('character_id', None)
        if character_id:
            queryset = queryset.filter(idGlavniLik__idGlavniLik=character_id)  
        return queryset
    
class GlavniLikViewSet(viewsets.ModelViewSet):
    queryset = GlavniLik.objects.all()
    serializer_class = GlavniLikSerializer

def get_queryset(self):
    queryset = GlavniLik.objects.all()
    search_term = self.request.query_params.get('searchTerm', None)
    if search_term is not None:
        queryset = queryset.filter(nazivGlavniLik__icontains=search_term)
    return queryset

