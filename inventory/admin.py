from django.contrib import admin
from .models import Item, Purchase, Sale


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    actions = []
    list_display = ('name', 'quantity', 'price', 'total_value')
    list_filter = ('quantity',)
    search_fields = ('name',)


    def total_value(self, obj):
        return (obj.quantity or 0) * (obj.price or 0)
    total_value.short_description = 'Total Value'


class PurchaseAdmin(admin.ModelAdmin):
    actions = []
    list_display = ('item', 'quantity', 'date')
    list_filter = ('date',)
    search_fields = ('item__name',)
    list_select_related = ('item',)


class SaleAdmin(admin.ModelAdmin):
    actions = []
    list_display = ('item', 'quantity', 'date')
    list_filter = ('date',)
    search_fields = ('item__name',)
    list_select_related = ('item',)


admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Sale, SaleAdmin)

