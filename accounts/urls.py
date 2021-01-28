"""
	PB system Application


	Filename; urls.py
	Date: Jan 25, 2021
	Written by Nobuharu Shimazu

"""

from django.urls import path
from . import views

app_name="accounts"


urlpatterns = [
	path("profile/<int:pk>", views.UserDetail.as_view(), name="user_detail"),
	path("profile/update/<int:pk>", views.UserUpdate.as_view(), name="user_update"),
]