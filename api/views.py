from psycopg2 import IntegrityError
from rest_framework import viewsets
from .models import GlavniLik, ListaZelja, Strip
from .serializers import GlavniLikSerializer, ListaZeljaSerializer, StripSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Kolekcija
from .serializers import KolekcijaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ListaZelja, Strip
from django.db.models import Count, F
from django.db.models import Prefetch
from django.db import models
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView

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
        search_term = self.request.query_params.get('searchTerm', None)

        if character_id:
            queryset = queryset.filter(idGlavniLik__idGlavniLik=character_id)

        if search_term:
            # You can adjust the filtering logic as needed
            queryset = queryset.filter(
                models.Q(nazivStrip__icontains=search_term) |
                models.Q(broj__icontains=search_term)
            )

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
    

class ListaZeljaViewSet(viewsets.ModelViewSet):
    queryset = ListaZelja.objects.all()
    serializer_class = ListaZeljaSerializer

class ListaZeljaGroupedByGlavniLik(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Prefetch related strips and order them by 'broj'
        user_wishlist = ListaZelja.objects.filter(
            idKorisnik=request.user
        ).select_related('idStrip').prefetch_related(
            Prefetch('idStrip', queryset=Strip.objects.order_by('broj'))
        ).order_by('idStrip__idGlavniLik')
        
        grouped_data = {}
        for item in user_wishlist:
            glavni_lik_id = item.idStrip.idGlavniLik.idGlavniLik
            if glavni_lik_id not in grouped_data:
                grouped_data[glavni_lik_id] = {
                    'idGlavniLik': glavni_lik_id,
                    'nazivGlavniLik': item.idStrip.idGlavniLik.nazivGlavniLik,
                    'items': []
                }
            grouped_data[glavni_lik_id]['items'].append(StripSerializer(item.idStrip).data)

        # Sort items in each group by 'broj'
        for key in grouped_data:
            grouped_data[key]['items'].sort(key=lambda x: x['broj'])

        response_data = list(grouped_data.values())
        return Response(response_data)
    
    def create(self, request, *args, **kwargs):
        user = request.user
        strip_id = request.data.get('idStrip')

        try:
            ListaZelja.objects.create(idKorisnik=user, idStrip_id=strip_id)
            return Response({"message": "Item successfully added to wishlist"}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"error": "This item is already in your wishlist"}, status=status.HTTP_400_BAD_REQUEST)

class ComicBookDetailView(RetrieveAPIView):
    queryset = Strip.objects.all()
    serializer_class = StripSerializer
    lookup_field = 'idStrip'  # Change this line to use 'idStrip' instead of 'id'



from .models import StatusOglasa, Stanje, Oglas
from .serializers import StatusOglasaSerializer, StanjeSerializer, OglasSerializer

class StatusOglasaViewSet(viewsets.ModelViewSet):
    queryset = StatusOglasa.objects.all()
    serializer_class = StatusOglasaSerializer

class StanjeViewSet(viewsets.ModelViewSet):
    queryset = Stanje.objects.all()
    serializer_class = StanjeSerializer

class OglasViewSet(viewsets.ModelViewSet):
    queryset = Oglas.objects.all()
    serializer_class = OglasSerializer

class OglasList(generics.ListAPIView):
    serializer_class = OglasSerializer

    def get_queryset(self):
        queryset = Oglas.objects.all()
        user_id = self.request.query_params.get('userId', None)  # Get user ID from query params
        comicbook_id = self.kwargs.get('comicbook_id', None)  # Get comicbook ID from the URL

        if user_id is not None:
            queryset = queryset.filter(idKorisnik_id=user_id)  # Filter by user ID

        if comicbook_id is not None:
            queryset = queryset.filter(idStrip_id=comicbook_id)  # Filter by comicbook ID

        return queryset
