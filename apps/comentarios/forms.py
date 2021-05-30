from django import forms
from django.forms.widgets import ClearableFileInput


from comentarios.models import Comentarios

class ComentariosForms(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = '__all__'
        widget= {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usuario', 'type':'hidden'}),
        }