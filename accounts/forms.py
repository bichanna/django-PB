"""
	Accounts form

	File name : forms.py
	Date :  Jan 27th, 2021
	Written by Nobuharu Shimazu
"""

from django.forms import ModelForm
from django.contrib.auth.models import User
from PBSystem.models import UserInfo

class UserUpdateForm(ModelForm):
	"""ユーザー情報更新フォーム"""
	class Meta:
		model = UserInfo
		fields = ("short_name")
		model = User
		fields = ("email", "username")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

