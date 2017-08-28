from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from models import *

class Regforms(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput
		(attrs={'class':'form-control'}),
		max_length=30,
		required=True)

	email = forms.CharField(widget=forms.EmailInput
		(attrs={'class':'form-control'}),
		max_length=30,
		required=True)

	password = forms.CharField(widget=forms.PasswordInput
		(attrs={'class':'form-control'}),
		max_length=30,
		required=True)

	confirm_password = forms.CharField(widget=forms.PasswordInput
		(attrs={'class':'form-control'}),
		max_length=30,
		label = "Confirm your Password",
		required=True)


	def clean_username(self):
		uname = self.cleaned_data['username']
		try:
			match = User.objects.get(username=uname)

		except:
			return self.cleaned_data['username']

		raise form.ValidationError('Username Already Exists')

	class Meta:
		model = User
		fields = ['username','email','password','confirm_password',]



class bloging(forms.ModelForm):

	class Meta:
		model = blogy
		fields = ['title','description','pic']






