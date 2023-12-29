from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GlavniLikViewSet, StripViewSet, KolekcijaViewSet, UserCollectionViewSet

router = DefaultRouter()
router.register(r'glavnilik', GlavniLikViewSet)
router.register(r'strip', StripViewSet)
router.register(r'kolekcija', KolekcijaViewSet)
router.register(r'usercollection', UserCollectionViewSet, basename='usercollection')
urlpatterns = [
    path('', include(router.urls)),
]