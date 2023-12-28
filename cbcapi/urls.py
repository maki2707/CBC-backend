from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GlavniLikViewSet

router = DefaultRouter()
router.register(r'characters', GlavniLikViewSet)

urlpatterns = [
    path('', include(router.urls)),
]