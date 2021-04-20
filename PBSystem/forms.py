"""
	form classes

	file name: PB/PBSystem/forms.py
	date: Jan 18th, 2021
"""


from django.forms import ModelForm
from django import forms
from .models import BankAccounts,Banks,UserType,User,BankAccountData,CustomerList
from django.conf import settings

class BankAccountDataForm(ModelForm):
	#date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
	class Meta:
		#モデルクラスを指定
		model = BankAccountData
		#モデルフィールドを指定
		fields = ("bank_accounts","banks", "bank_branch_name", "bank_address", "banker_1", "banker_2", "date", "bank_account", "bank_account_holder")
		labels = {
			"bank_accounts": "Customer Account",
			"banks": "Bank",
			"bank_branch_name": "Bank branch name",
			"bank_address": "Bank branhc address",
			"banker_1": "Banker 1",
			"banker_2": "Banker 2 (optional)",
			"date": "Date",
			"bank_account": "Bank account",
			"bank_account_holder": "Bank account holder's name",
		}


class SearchForm(forms.Form):
	"""
		表検索用のフォーム
	"""
	key_word = forms.CharField(
		required=False,
		widget= forms.TextInput(attrs={"placeholder":" search..."})   # this is how to put a place holder
	)




class NewBankAccount(ModelForm):
	class Meta:
		model = BankAccounts
		fields = ("bank_account_number", "customer_name")
		labels = {
			"bank_account_number": "Bank account number",
			"customer_name" : "Customer",
		}


class NewCustomer(ModelForm):
	class Meta:
		model = CustomerList
		fields = ("customer_name",)
		labels = {
			"customer_name" : "New customer name",
		}

#class NewAccountForCustomer(ModelForm):
#	class Meta:
#		model = BankAccounts
#		fields = (,)
#		labels = {
#
#		}
			








