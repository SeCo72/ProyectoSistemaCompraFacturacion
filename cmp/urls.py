from django.urls import path, include

from .views import ProveedorView, ProveedorNew, ProveedorEdit, ProveedorInactivar, ComprasView, compras, CompraDetDelete

from .reportes import reporte_compras, imprimir_compra

app_name = 'cmp'

urlpatterns = [
    path('Proveedor/', ProveedorView.as_view(), name='proveedor_list'), 
    path('Proveedor/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('Proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('Proveedor/inactivar/<int:id>', ProveedorInactivar, name='proveedor_inactivar'), 

    path('compras/',ComprasView.as_view(), name="compras_list"),
    path('compras/new',compras, name="compras_new"),
    path('compras/edit/<int:compra_id>',compras, name="compras_edit"),
    path('compras/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(), name="compras_del"),

     path('compras/listado', reporte_compras, name='compras_print_all'),
     path('compras/<int:compra_id>/imprimir', imprimir_compra,name="compras_print_one"),
]


