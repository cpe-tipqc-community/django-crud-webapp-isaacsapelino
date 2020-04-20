from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 

class CreateUserForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'Email Address'}))
	class Meta:
		model = User 
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
		widgets = {
			'first_name' : forms.TextInput(attrs={
					'class' : 'form-control input-box-text',
					'placeholder' : 'First name'
				}),
			'last_name' : forms.TextInput(attrs={
					'class' : 'form-control input-box-text',
					'placeholder' : 'Last name'
				}),
			'username' : forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Username'
				}),
			'password1' : forms.PasswordInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Password'
				}),
			'password2' : forms.PasswordInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Confirm Password'
				})
		}