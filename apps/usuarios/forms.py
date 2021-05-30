from django import forms
from django.forms.widgets import ClearableFileInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from usuarios.models import Usuario
from django.contrib.auth.models import User


class CriarUsuarioForms(forms.ModelForm):
    foto_usuario   = forms.ImageField(widget = ClearableFileInput)

    class Meta:
        model = Usuario
        fields = ('__all__')




class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )


	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		

class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2')
