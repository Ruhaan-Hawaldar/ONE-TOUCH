from django.contrib import admin
from .models import Service, PickupRequest


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(PickupRequest)
class PickupRequestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'service',
        'pickup_date',
        'status',
        'created_at',
    )

    list_filter = ('status', 'service', 'pickup_date')
    search_fields = ('name', 'phone', 'address')
    list_editable = ('status',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 25
