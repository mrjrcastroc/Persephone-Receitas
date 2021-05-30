from django import forms
from django.forms.widgets import ClearableFileInput


from receitas.models import Receita

class ReceitaForms(forms.ModelForm):
    foto_receita   = forms.ImageField(widget = ClearableFileInput)
    foto_receita2  = forms.ImageField(widget = ClearableFileInput)
    foto_receita3  = forms.ImageField(widget = ClearableFileInput)

    class Meta:
        model = Receita
        exclude = ('likes',)
        widgets={
            'usuario' : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),

        }

class EditarReceitaForms(forms.ModelForm):
    foto_receita   = forms.ImageField(widget = ClearableFileInput)
    foto_receita2  = forms.ImageField(widget = ClearableFileInput)
    foto_receita3  = forms.ImageField(widget = ClearableFileInput)

    class Meta:
        model = Receita
        exclude = ('likes',)
        widgets={
            'usuario' : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),

        }

