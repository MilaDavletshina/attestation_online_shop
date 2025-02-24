from django.contrib import admin
from .models import Contact, Product, NetworkLink


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')


class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'get_supplier', 'debt', 'created_at')
    list_filter = ('contact__city',)
    actions = ['clear_debt']

    def get_supplier(self, obj):
        return obj.supplier.name if obj.supplier else 'No Supplier'
    get_supplier.short_description = 'Supplier'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
    clear_debt.short_description = "Clear debt for selected nodes"


admin.site.register(Contact, ContactAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(NetworkLink, NetworkLinkAdmin)