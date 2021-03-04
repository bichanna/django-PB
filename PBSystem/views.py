"""
	PBSystem application

	File name: views.py
	Date: Jan 11, 2021
	Written by Nobuharu Shimazu
"""

from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import View,ListView,DeleteView,UpdateView, CreateView
from django.utils import timezone
from .models import CustomerList,BankAccounts,Banks,UserType,User,BankAccountData
from .forms import BankAccountDataSearchForm,BankAccountDataForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
"""
class PBSystemBankAccountDataListView(View):
	def get(self, request, *args, **kwargs):

		context = {}
		# 入力されたすべての情報を取得
		bank_account_datas = BankAccountData.objects.all()
		context["bank_account_datas"] = bank_account_datas
		return render(request, "PBSystem/bank_account_data_list.html", context)

bank_account_data_list = PBSystemBankAccountDataListView.as_view()
"""


class PBSystemBankAccountDataListView(ListView):
	"""
		Get Request用の処理
	"""
	model = BankAccountData
	template_name = "PBsystem/bank_account_data_list.html"
	paginate_by = 8


	def get_queryset(self):
		"""
			検索条件の設定
		"""
		#フォームを設定。
		form = BankAccountDataSearchForm(self.request.GET or None)
		self.form = form

		queryset = super().get_queryset()
		if form.is_valid():
			key_word = form.cleaned_data.get('key_word')
			if key_word:
				for word in key_word.split():
					queryset = queryset.filter(Q(bank_accounts__icontains=word) | Q(banks__icontains=word) | Q(bank_branch_name__icontains=word) | Q(bank_address__icontains=word) | Q(banker_1__icontains=word) | Q(banker_2__icontains=word) | Q(regdate__icontains=word) | Q(bank_account__icontains=word) | Q(bank_account_holder__icontains=word))

		return queryset


	def get_context_data(self, **kwargs):
		"""
			コンテキストの設定。
		"""

		context = super().get_context_data(**kwargs)
		context["form"] = self.form
		print("CONTEXT  ", context)
		return context

bank_account_data_list = PBSystemBankAccountDataListView.as_view()


class AdminUserListListView(ListView):
	"""
		admin listとuser listのページ用
	"""
	model = User
	template_name = "PBSystem/admin_user_list_list.html"
	paginate_by = 10

	def get_queryset(self):
		status = self.request.GET.get('usertype')
		print(status, "⭐"*10)
		queryset = super().get_queryset()
		queryset = queryset.filter(user_type__user_type=status)
		return queryset

	def get_context_data(self, **kwargs):
		"""
			コンテキストの設定。
		"""

		context = super().get_context_data(**kwargs)
		status = self.request.GET.get('usertype')
		context["status"] = status
		#print("CONTEXT  ", context)
		return context
admin_user_list_list = AdminUserListListView.as_view()




class CreateNewCustomerView(LoginRequiredMixin, CreateView):
	model = "BankAccountData"
	template_name = "PBSystem/new_customer_creation.html"
	form_class = BankAccountDataForm

	def form_valid(self, form):
		print("⭐"*10)
		print(self.request.user.id)
		print(User.objects.get(id=self.request.user.id))
		print(form.instance)
		user_id = User.objects.get(id=self.request.user.id)

		form.instance.user_info = user_id
		return super().form_valid(form)

	def get_success_url(self):
		"""詳細画面にリダイレクトする。"""
		return reverse("PBSystem:bank_account_data_list",)



create_new_customer = CreateNewCustomerView.as_view()



class BankAccountDataDelete(LoginRequiredMixin, DeleteView):
	model = BankAccountData
	template_name = "PBSystem/bank_account_data_delete.html"
	def get_success_url(self):
		"""一覧ページにリダイレクトする。"""
		return reverse("PBSystem:bank_account_data_list")




























