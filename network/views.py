from rest_framework import viewsets, filters

from .models import NetworkNode
from .permissions import IsActiveUser
from .serializers import NetworkNodeSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']  # Фильтрация по стране
    permission_classes = [IsActiveUser]  # Доступ только для авторизованных или активных пользователей

