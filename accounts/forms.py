"""
	Accounts form

	File name : forms.py
	Date :  Jan 27th, 2021
	Written by Nobuharu Shimazu
"""

from django.forms import ModelForm
from django.contrib.auth.models import User
from PBSystem.models import User
from django import forms

class UserUpdateForm(ModelForm):
	""""""
	class Meta:
		
		model = User
		fields = ("username","short_name","email")
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'





"""
class UserUpdateForm(forms.Form):
	short_name = forms.CharField(label="Short Name",required=False)
	email = forms.CharField(label="E-mail",required=False)
	username = forms.CharField(label="User Name",required=False)

"""