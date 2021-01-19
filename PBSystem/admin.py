"""
	PBSystem application
	admin用の設定

	File name: admin.py
	Date: Jan 11, 2021
	Written by Nobuharu Shimazu
"""

from django.contrib import admin
from .models import CustomerList,BankAccounts,Banks,UserType,UserInfo,BankAccountData

admin.site.register(CustomerList)
admin.site.register(BankAccounts)
admin.site.register(Banks)
admin.site.register(UserType)
admin.site.register(UserInfo)
admin.site.register(BankAccountData)