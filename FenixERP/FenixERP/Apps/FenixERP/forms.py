from django import forms
from .models import ProductoTienda



class NameForm(forms.Form):
    Nombre = forms.CharField(max_length=100)
