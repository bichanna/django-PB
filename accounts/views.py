"""
	Accoutns 表示部分

	Filename views.py
	Date: 2021.1.17
	Written by Nobuharu Shimazu

"""

from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, CreateView
from .forms import UserUpdateForm
from django.contrib.auth.models import User
from django.shortcuts import resolve_url
from django.urls import reverse_lazy

# Create your views here.
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
		return resolve_url("accounts:user_detail",pk=self.kwargs["pk"])


"""
class UserCreate(CreateView):
"""
		#ユーザー作成用のビュー
"""
	template_name="registration/user_create.html"
	form_class=UserCreateForm
	success_url = reverse_lazy("login")
"""

