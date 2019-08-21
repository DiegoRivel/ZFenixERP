import django_tables2 as tables
from django_tables2.utils import A
from .models import ProductoTienda


class tablaProducto(tables.Table):
    class Meta:
        model = ProductoTienda
        attrs = {'class': 'table table-dark table-responsive-lg', 'border': "5px solid", 'style': "width:100%"}
        fields = ('Nombre', 'Tienda', 'Precio')
        #template = 'table-blocks.html'
        #template_name = 'django_tables2/table.html'


class tablaProducto2(tables.Table):
    Nombre = tables.Column(verbose_name="Nombre")
    Tienda = tables.Column(verbose_name="Tienda")
    Precio  = tables.Column(verbose_name="Precio")
    class Meta:
        model = ProductoTienda
        attrs = {'class': 'table table-dark table-responsive-lg', 'border': "5px solid", 'style': "width:90%"}
        fields = ('Nombre', 'Tienda', 'Precio')
        #template = 'table-blocks.html'
        #template_name = 'django_tables2/table.html'

