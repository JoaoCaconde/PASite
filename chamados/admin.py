from django.contrib import admin
from chamados.models import ChamadoRPAEntradaManual,CompletedChamadoRPAEntradaManual
from .forms import ChamadoRPAEntradaManualForm
from import_export import resources
from django.forms import TextInput
from django.db import models
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.models import LogEntry
import xml.etree.ElementTree as ET


LogEntry.objects.all().delete()


class ChamadoRPAEntradaManualResource(resources.ModelResource):
    
    
    class Meta:
        model = ChamadoRPAEntradaManual
        fields = ('owner', 'title', 'key', 'value', 'type_nf', 'frete', 'cnpj_fornecedor', 'cnpj_cliente', 'cnpj_transportadora')
        import_id_fields = ('title', 'key', 'value', 'type_nf', 'frete', 'cnpj_fornecedor', 'cnpj_cliente', 'cnpj_transportadora')
    
    
    def __init__(self, request=None, **kwargs):
        super().__init__(**kwargs)
        self.request = request  # Store request to access the user
    
    def before_import_row(self, row, row_number=None, **kwargs):
        # If the user column is missing or empty in the imported file
        if not row.get('owner') and self.request and self.request.user:
            row['owner'] = self.request.user.id
            
            
class ChamadoRPAEntradaManualAdmin(ImportExportModelAdmin):
    form = ChamadoRPAEntradaManualForm
    resource_class = ChamadoRPAEntradaManualResource
    list_display = ('status', 'created_at', 'key', 'value', 'type_nf', 'cnpj_fornecedor', 'cnpj_cliente', 'frete', 'cnpj_transportadora')
    search_fields = ('title','value', 'key', 'cnpj_fornecedor', 'cnpj_cliente', 'cnpj_transportadora')
    readonly_fields = ('status','message')
    exclude = ('owner',) 
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50', 'style': 'width: 400px;'})},
    }
    
    class Media:
        js = ('admin/js/populate_xml.js',)
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)
    
    def has_change_permission(self, request, obj=None):
        # If obj exists, it means it is already submitted/saved in the DB
        if obj is not None:
            return False
        return super().has_change_permission(request, obj)
    
    def get_queryset(self, request, obj=None):
        if obj is not None: 
            return False
        return super().get_queryset(request).filter(owner=request.user, status__in=[ChamadoRPAEntradaManual.Status.PENDING, ChamadoRPAEntradaManual.Status.RETURNED])
    
    def get_import_resource_kwargs(self, request, *args, **kwargs):
        # Pass the request context down to the resource instance
        super().get_import_resource_kwargs(request, *args, **kwargs)
        kwargs['request'] = request
        return kwargs 
 
    
class CompletedChamadoRPAEntradaManualAdmin(admin.ModelAdmin):
    list_display = ('status', 'created_at', 'key', 'value', 'type_nf', 'frete', 'message')
    list_filter = ('created_at',)
    search_fields = ('title', 'owner__name')
    exclude = ('owner',)
    
    def has_change_permission(self, request, obj=None):
        # If obj exists, it means it is already submitted/saved in the DB
        if obj is not None:
            return False
        return super().has_change_permission(request, obj)
    
    def get_queryset(self, request, obj=None):
        if obj is not None: 
            return False
        return super().get_queryset(request).filter(status=ChamadoRPAEntradaManual.Status.FINISHED)
    
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(ChamadoRPAEntradaManual, ChamadoRPAEntradaManualAdmin)
admin.site.register(CompletedChamadoRPAEntradaManual, CompletedChamadoRPAEntradaManualAdmin)
