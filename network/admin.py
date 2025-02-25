from django.contrib import admin
from .models import Contact, Product, NetworkLink


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')


class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'supplier', 'debt', 'created_at')
    list_filter = ('contact__city',)
    actions = ['clear_debt']

    def supplier(self, obj):
        """admin: ссылка на «Поставщика» под названием модели в карточке."""
        return obj.supplier.name if obj.supplier else 'No Supplier'
    supplier.short_description = 'Supplier'

    def clear_debt(self, request, queryset):
        """admin action: Очистка задолженности у выбранных объектов."""
        queryset.update(debt=0)
    clear_debt.short_description = "Очистить задолженность"


admin.site.register(Contact, ContactAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(NetworkLink, NetworkLinkAdmin)
