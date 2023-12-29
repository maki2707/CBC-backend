from rest_framework import viewsets
from .models import GlavniLik, Strip
from .serializers import GlavniLikSerializer, StripSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Kolekcija
from .serializers import KolekcijaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
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

    def get_serializer_context(self):
        # Pass the request context to the serializer
        return {'request': self.request}
    
class GlavniLikViewSet(viewsets.ModelViewSet):
    queryset = GlavniLik.objects.all()
    serializer_class = GlavniLikSerializer

def get_queryset(self):
    queryset = GlavniLik.objects.all()
    search_term = self.request.query_params.get('searchTerm', None)
    if search_term is not None:
        queryset = queryset.filter(nazivGlavniLik__icontains=search_term)
    return queryset



class KolekcijaViewSet(viewsets.ModelViewSet):
    queryset = Kolekcija.objects.all()
    serializer_class = KolekcijaSerializer

    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    def remove(self, request, *args, **kwargs):
        user_id = request.query_params.get('userId')
        comic_id = request.query_params.get('comicId')
        if user_id and comic_id:
            try:
                kolekcija = Kolekcija.objects.get(idKorisnik_id=user_id, idStrip_id=comic_id)
                kolekcija.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Kolekcija.DoesNotExist:
                return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)




class UserCollectionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StripSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        user = self.request.user
        character_id = self.request.query_params.get('character_id', None)

        if user.is_authenticated and character_id:
            # Filter strips based on the character_id and return the queryset
            return Strip.objects.filter(idGlavniLik__idGlavniLik=character_id)
        # Return an empty queryset if conditions are not met
        return Strip.objects.none()