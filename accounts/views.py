"""
	Accoutns 表示部分

	Filename views.py
	Date: 2021.1.17
	Written by Nobuharu Shimazu

"""

from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, View
from .forms import UserUpdateForm, UserCreateForm
from django.contrib.auth.models import User
from django.shortcuts import resolve_url, reverse, render
from django.urls import reverse_lazy
from PBSystem.models import User, UserType


class UserCreate(CreateView):
	"""
		ユーザー作成用のビュー
	"""
	template_name = "registration/user_create.html"
	form_class = UserCreateForm
	model = User

	def form_valid(self, form):

		usertype = UserType.objects.get(user_type=self.request.GET.get("usertype"))
		
		form.instance.user_type = usertype

		return super().form_valid(form)


	def get_success_url(self):
		"""詳細画面にリダイレクトする。"""
		return reverse("PBSystem:bank_account_data_list",)




class OnlyYouMixin(UserPassesTestMixin):
	raise_exception = True

	def test_func(self):
		"""
			ユーザーが一致する場合とスーパーユーザーの場合許可する。
		"""
		user = self.request.user
		return user.pk == self.kwargs["pk"] or user.is_superuser


class UserDetail(OnlyYouMixin, DetailView):
	"""
		ユーザーの詳細を表示するビュー
	"""

	model =User
	template_name = "accounts/user_detail.html"


class UserUpdate(OnlyYouMixin,UpdateView):
	"""
		ユーザーデータの更新をするためのレビュー
	"""
	model = User
	form_class = UserUpdateForm
	template_name = "accounts/user_form.html"


	def get_success_url(self):
		"""
			更新後の表示をする画面。ユーザーの詳細を表示する画面に遷移する。
		"""
		return resolve_url("PBSystem:bank_account_data_list",)

class UserDelete(OnlyYouMixin, View):
	template_name = "PBSystem/admin_user_list_list.html"
	def get(self, request, *args, **kwargs):
	
		User.objects.get(id=kwargs["pk"]).delete()
		return render(request, self.template_name)





