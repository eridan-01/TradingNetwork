from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import NetworkNode


@admin.action(description='Очистка задолженности')
def clear_debt(queryset):
    queryset.update(debt=0)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_filter = ['city']
    list_display = ['name', 'country', 'city', 'supplier_link', 'debt']
    actions = [clear_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            link = reverse('admin:network_networknode_change', args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier.name)
        return '-'
    supplier_link.short_description = 'Поставщик'
