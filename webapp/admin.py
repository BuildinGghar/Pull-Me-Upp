from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'service_type', 'description')
    list_filter = ('service_type',)
    search_fields = ('title', 'description')
    ordering = ('title',)
