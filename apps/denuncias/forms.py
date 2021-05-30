from django import forms
from django.forms.widgets import ClearableFileInput


from denuncias.models import CategoriaDenuncia, DenunciaReceita

# Categorias

class CategoriaDenunciaForms(forms.ModelForm):
    class Meta:
        model = CategoriaDenuncia

        fields = '__all__'
        

class EditarCategoriaDenunciaForms(forms.ModelForm):
    class Meta:
        model = CategoriaDenuncia
        fields = '__all__'


# Denuncia de Receitas


class DenunciaReceitaForms(forms.ModelForm):
    class Meta:
        model = DenunciaReceita
        fields = '__all__'

class ResolverDenunciaReceitaForms(forms.ModelForm):
    class Meta:
        model = DenunciaReceita
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'disabled ': 'disabled '}),
            'receita': forms.TextInput(attrs={'disabled': 'disabled'}),
            'usuario_denunciado': forms.TextInput(attrs={'disabled': 'disabled'}),
            'usuario_efetuou_denuncia': forms.TextInput(attrs={'disabled': 'readonly'}),
            'categoria_denuncia': forms.TextInput(attrs={'disabled': 'disabled'}),
            
        }


