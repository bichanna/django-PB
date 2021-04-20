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
	path("admin_user_list/",views.admin_user_list_list, name="admin_user_list_list"),
	path("create_new_data/", views.create_new_data, name="newData"),
	path("register_new_customer/", views.register_new_customer, name="newCustomer"),
	path("bank_account_data/<int:pk>/delete/", views.BankAccountDataDeleteView.as_view(), name="bank_account_data_delete"),
	path("customer_list/", views.CustomerListListView.as_view(), name="go-to-customerlist"),
	path("customer_list/<int:pk>/delete/", views.CustomerDeleteView.as_view(), name="customer_deletion"),
	path("customer_list/<int:pk>/makeaccount/",views.CreateAccountView.as_view(), name="makeNewAccount"),
]
