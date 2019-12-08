from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *


class OferenteResource(resources.ModelResource):
    class Meta:
        model = Oferente


class OferenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'fecha_creacion')
    resource_class = OferenteResource


class InspectorResource(resources.ModelResource):
    class Meta:
        model = Oferente


class InspectorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'fecha_creacion')
    resource_class = OferenteResource


# Registro de modelos en la app de admin
admin.site.register(Oferente, OferenteAdmin)
admin.site.register(Inspector, InspectorAdmin)
