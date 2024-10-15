from django.urls import path, include
from .views import ProveedorView, ProveedorNew, ProveedorEdit, ProveedorInactivar

app_name = 'cmp'

urlpatterns = [
    path('Proveedor/', ProveedorView.as_view(), name='proveedor_list'), 
    path('Proveedor/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('Proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('Proveedor/inactivar/<int:id>', ProveedorInactivar, name='proveedor_inactivar'), 
]


