from rest_framework import viewsets
from .models import NetworkLink
from .permissions import IsActive
from .serializers import NetworkLinkSerializer, NetworkLinkCreateSerializer
from rest_framework.permissions import IsAuthenticated


class NetworkLinkViewSet(viewsets.ModelViewSet):
    """Простой ViewSet-класс для вывода списка торговых сетей и информации по одному объекту."""
    queryset = NetworkLink.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

    def get_serializer_class(self):
        """Метод возвращает сериалайзер, в соответствии с заданным условием."""
        if self.action in ['create', 'update', 'partial_update']:
            return NetworkLinkCreateSerializer
        return NetworkLinkSerializer

    def get_queryset(self):
        """Настраиваем выборку данных из БД по параметру - фильтрация объектов по определенной стране"""
        queryset = super().get_queryset()
        country = self.request.query_params.get('country', None)
        if country:
            queryset = queryset.filter(contact__country=country)
        return queryset

