from django import forms

class loginform(forms.Form):
	name=forms.CharField(max_length=150)
	password=forms.CharField(max_length=150,widget=forms.PasswordInput)

class CreateUserForm(forms.Form):
	username=forms.CharField(max_length=150)
	password=forms.CharField(max_length=150,widget=forms.PasswordInput)
	email=forms.CharField(max_length=150)
