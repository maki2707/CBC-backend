from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GlavniLikViewSet, StripViewSet

router = DefaultRouter()
router.register(r'glavnilik', GlavniLikViewSet)
router.register(r'strip', StripViewSet)

urlpatterns = [
    path('', include(router.urls)),
]