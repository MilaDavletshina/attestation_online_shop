from django.contrib import admin

from .models import Contact, NetworkLink, Product


class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "country", "city", "street", "house_number")
    list_filter = (
        "email",
        "country",
        "city",
        "street",
        "house_number",
    )
    search_fields = (
        "email",
        "country",
        "city",
        "street",
        "house_number",
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date")
    list_filter = (
        "name",
        "model",
    )
    search_fields = (
        "name",
        "model",
    )


class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "supplier", "debt", "created_at")
    list_filter = ("contact__city",)
    actions = ["clear_debt"]

    def supplier(self, obj):
        """admin: ссылка на «Поставщика» под названием модели в карточке."""
        return obj.supplier.name if obj.supplier else "No Supplier"

    supplier.short_description = "Supplier"

    def clear_debt(self, request, queryset):
        """admin action: Очистка задолженности у выбранных объектов."""
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность"


# Связываем модель с классом администрирования.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(NetworkLink, NetworkLinkAdmin)
