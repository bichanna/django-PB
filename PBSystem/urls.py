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

]