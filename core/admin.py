from django.contrib import admin

from core.models import Fabricante, Categoria, Produto, Compra, ItensCompra

admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Produto)

"""
admin.site.register(Compra)
admin.site.register(ItensCompra)
"""


class ItensInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)
