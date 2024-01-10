from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComicBookDetailView, GlavniLikViewSet, ListaZeljaGroupedByGlavniLik, ListaZeljaViewSet, OglasList, OglasViewSet, StanjeViewSet, StatusOglasaViewSet, StripViewSet, KolekcijaViewSet, UserCollectionViewSet

router = DefaultRouter()
router.register(r'glavnilik', GlavniLikViewSet)
router.register(r'strip', StripViewSet)
router.register(r'kolekcija', KolekcijaViewSet)
router.register(r'usercollection', UserCollectionViewSet, basename='usercollection')
router.register(r'listazelja', ListaZeljaViewSet)
router.register(r'statusoglasa', StatusOglasaViewSet)
router.register(r'stanje', StanjeViewSet)
router.register(r'oglas', OglasViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('lista-zelja/grouped/', ListaZeljaGroupedByGlavniLik.as_view(), name='lista-zelja-grouped'),
    path('comicbook/<int:idStrip>/', ComicBookDetailView.as_view(), name='comicbook-detail'),
    path('oglasi/user/<int:userId>/', OglasList.as_view(), name='oglasi-user-list'),
    path('oglasi/comicbook/<int:comicbook_id>/', OglasList.as_view(), name='oglasi-comicbook-list'),
]

