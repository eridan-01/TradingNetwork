from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import NetworkConfig
from .views import NetworkNodeViewSet


app_name = NetworkConfig.name

router = DefaultRouter()
router.register(r'networknodes', NetworkNodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
