"""
	PBSystem application

	File name: urls.py
	Date: Jan 11, 2021
	Written by Nobuharu Shimazu
"""
 
from django.urls import path
from . import views


app_name = "PBSystem"  # application name
urlpatterns = [
	path("", views.bank_account_data_list, name="bank_account_data_list"),
	path("admin-user-list/",views.admin_user_list_list, name="admin_user_list_list"),
	path("create-ne-data/", views.create_new_data, name="newData"),
	path("register-new-customer/", views.register_new_customer, name="newCustomer"),
	path("bank-account-data/<int:pk>/delete/", views.BankAccountDataDeleteView.as_view(), name="bank_account_data_delete"),
	path("customer-list/", views.CustomerListListView.as_view(), name="go-to-customerlist"),
	path("customer-list/<int:pk>/delete/", views.CustomerDeleteView.as_view(), name="customer_deletion"),
	path("customer-list/makeaccount/",views.CreateBankAccountView.as_view(), name="makeNewAccount"),
]
