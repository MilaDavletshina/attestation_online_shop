from django.db import models


class Contact(models.Model):
    email = models.EmailField(unique=True, verbose_name="Электронная почта", help_text="Укажите электронную почту")
    country = models.CharField(max_length=100, verbose_name="Страна", help_text="Укажите страну")
    city = models.CharField(max_length=100, verbose_name="Город", help_text="Укажите город")
    street = models.CharField(max_length=100, verbose_name="Улица", help_text="Укажите название улицы")
    house_number = models.CharField(max_length=100, verbose_name="Дом", help_text="Укажите номер дома")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.house_number}"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Укажите название")
    model = models.CharField(max_length=100, verbose_name="Модель", help_text="Укажите модель")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок", help_text="Укажите дату выхода продукта на рынок")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name}, {self.model}"


class NetworkLink(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Укажите название")
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name="Контакт", help_text="Укажите контакт")
    products = models.ManyToManyField(Product, verbose_name="Продукт", help_text="Укажите продукт")
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Поставщик", help_text="Укажите поставщика")
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Задолженность перед поставщиком", help_text="Укажите задолженность перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

    def __str__(self):
        return f"{self.name}"

    def get_level(self):
        level = 0
        supplier = self.supplier
        while supplier:
            level += 1
            supplier = supplier.supplier
        return level
