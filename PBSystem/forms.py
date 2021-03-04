"""
	form classes

	file name: PB/PBSystem/forms.py
	date: Jan 18th, 2021
"""


from django.forms import ModelForm
from django import forms
from .models import CustomerList,BankAccounts,Banks,UserType,User,BankAccountData

class BankAccountDataForm(ModelForm):
	"""
		
	"""
	class Meta:
		#モデルクラスを指定
		model = BankAccountData
		#モデルフィールドを指定
		fields = ("bank_accounts", "banks", "bank_branch_name", "bank_address", "banker_1", "banker_2", "bank_account", "bank_account_holder", "date")
		labels = {
			"bank_accounts": "Tên khách",
			"banks": "Tên ngân hàng",
			"bank_branch_name": "Chi nhánh",
			"bank_address": "Địa chỉ chi nhánh",
			"bank_account": "Số tài khoản",
			"banker_1": "Tên người phía ngân hàng 1",
			"banker_2": "Tên người phía ngân hàng 2",
			"bank_account_holder": "Chủ tài khỏan",
			"date": "Ngày tháng năm",
		}


class BankAccountDataSearchForm(forms.Form):
	"""
		表検索用のフォーム
	"""
	key_word = forms.CharField(label="検索キーワード",required=False)
