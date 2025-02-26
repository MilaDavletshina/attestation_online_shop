from rest_framework import serializers

from network.models import Contact, Product, NetworkLink


class ContactSerializer(serializers.ModelSerializer):
    """Преобразование данных модели "Контакты" из БД в нужный формат."""
    class Meta:
        model = Contact
        fields = "__all__" # Включаем все поля модели


class ProductSerializer(serializers.ModelSerializer):
    """Преобразование данных модели "Продукт" из БД в нужный формат."""
    class Meta:
        model = Product
        fields = "__all__" # Включаем все поля модели


class NetworkLinkSerializer(serializers.ModelSerializer):
    """Преобразование данных модели "Торговая сеть" из БД в нужный формат."""

    # указываем серилизаторы отдельных объектов, чтобы данные этих объектов отображалались корректно в API
    contact = ContactSerializer() # используем "OneToOneField" - это отдельный объект
    products = ProductSerializer(many=True) # используем "ManyToManyField" - это список объектов

    class Meta:
        model = NetworkLink
        fields = '__all__' # Включаем все поля модели
        read_only_fields = ('debt',) # указываем поля доступные только для чтения


class NetworkLinkCreateSerializer(serializers.ModelSerializer):
    """Создание и обновление объектов модели "Торговая сеть."""
    class Meta:
        model = NetworkLink
        fields = '__all__' # Включаем все поля модели
        read_only_fields = ('debt',) # указываем поля доступные только для чтения