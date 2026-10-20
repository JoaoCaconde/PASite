from django.contrib import admin
from costumers.models import Costumer
from import_export import resources


@admin.register(Costumer)
class CostumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'cpf', 'phone')
    list_filter = ('created_at', 'updated_at')
