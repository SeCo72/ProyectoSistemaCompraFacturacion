from django import forms
from .models import Categoria,SubCategoria,Marca, UnidadMedida,Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado'] 
        labels = {
            'descripcion': "Descripcion de la categoria",
            'estado': "Estado"
        }
        widgets = {
            'descripcion': forms.TextInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
#form para el de subcategoria 
class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model = SubCategoria
        fields = ['categoria','descripcion', 'estado'] 
        labels = {
            'descripcion': "Sub categoria",
            'estado': "Estado"}
        widgets = {
            'descripcion': forms.TextInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            }) 
        self.fields['categoria'].empty_label = "Seleccione Categoría"

#marca
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion', 'estado'] 
        labels = {
            'descripcion': "Descripcion de la Marca",
            'estado': "Estado"
        }
        widgets = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class UMForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion', 'estado'] 
        labels = {
            'descripcion': "Descripcion de la Unidad de Medida",
            'estado': "Estado"
        }
        widgets = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'codigo_barra', 'descripcion', 'estado', 
                  'precio', 'existencia', 'ultima_compra', 
                  'marca', 'subcategoria', 'unidad_medida']
        exclude = ['um', 'fm', 'uc', 'fc']
        widgets = {
            'descripcion': forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        # Cambia widget_attrs a widget.attrs
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True
        