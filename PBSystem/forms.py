"""
	form classes

	file name: PB/PBSystem/forms.py
	date: Jan 18th, 2021
"""


from django.forms import ModelForm
from django import forms
from .models import CustomerList,BankAccounts,Banks,UserType,UserInfo,BankAccountData

class BankAccountDataForm(ModelForm):
	"""
		
	"""
	class Meta:
		#モデルクラスを指定
		model = BankAccountData
		#モデルフィールドを指定
		fields = ()
		labels = {
		}


class BankAccountDataSearchForm(forms.Form):
	"""
		表検索用のフォーム
	"""
	key_word = forms.CharField(label="検索キーワード",required=False)
