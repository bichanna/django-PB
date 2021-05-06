"""
	PBSystem application

	File name: views.py
	Date: Jan 11, 2021
	Written by Nobuharu Shimazu
"""

from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import View,ListView,DeleteView,UpdateView, CreateView
from django.utils import timezone
from .models import *
from .forms import *
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
	template_name = "PBSystem/bank_account_data_list.html"
	paginate_by = 10


	def get_queryset(self):
		"""
			検索条件の設定
		"""
		#フォームを設定。
		form = SearchForm(self.request.GET or None)
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
		return context
admin_user_list_list = AdminUserListListView.as_view()


class CustomerListListView(ListView):
	"""
		the page of customer list 
	"""
	model = CustomerList
	template_name = "PBSystem/customer-list-page.html"
	paginate_by = 10
	form_class = SearchForm
	def get_queryset(self):
		form = SearchForm(self.request.GET or None)
		self.form = form

		queryset = super().get_queryset()
		if form.is_valid():
			key_word = form.cleaned_data.get('key_word')
			if key_word:
				for word in key_word.split():
					#queryset = queryset.filter(customer_name__icontains=word)
					queryset = queryset

		return queryset

customerlist_list = CustomerListListView.as_view()
	



class CreateNewDataView(LoginRequiredMixin, CreateView):
	model = BankAccountData
	template_name = "PBSystem/new_data_creation.html"
	form_class = BankAccountDataForm

	def form_valid(self, form):
		user_id = User.objects.get(id=self.request.user.id)

		form.instance.user_info = user_id
		# print("⭐"*10)
		# print(type(form.instance))
		return super().form_valid(form)

	def get_success_url(self):
		"""詳細画面にリダイレクトする。"""
		return reverse("PBSystem:bank_account_data_list",)

create_new_data = CreateNewDataView.as_view()



class CreateNewCustomerView(LoginRequiredMixin, CreateView):
	model = "CustomerList"
	template_name = "PBSystem/new-customer-registration.html"
	form_class = NewCustomer
	def form_valid(self, form):
		form.instance.save()
		customer_name = form.instance
		accountData = BankAccounts(bank_account_number="account1", customer_name=customer_name)
		accountData.save()
		return super().form_valid(form)

	def get_success_url(self):
		"""詳細画面にリダイレクトする。"""
		return reverse("PBSystem:go-to-customerlist",)

register_new_customer = CreateNewCustomerView.as_view()


class CreateBankAccountView(LoginRequiredMixin, CreateView):
	model = BankAccounts
	template_name = "PBSystem/create-new-account.html"
	form_class = NewAccount

	def form_valid(self, form):
		form.instance.customer_name = CustomerList.objects.get(id=self.request.GET.get("i"))
		form.instance.bank_account_number = "account"+str(BankAccounts.objects.filter(customer_name=form.instance.customer_name).count()+1)
		return super().form_valid(form)
	
	def get_success_url(self):
		"""詳細画面にリダイレクトする。"""
		return reverse("PBSystem:go-to-customerlist",)


createaccount = CreateBankAccountView.as_view()



class BankAccountDataDeleteView(DeleteView,LoginRequiredMixin):
	template_name = "PBSystem/bank_account_data_list_delete.html"
	model = BankAccountData
	def get_success_url(self):
		"""一覧ページにリダイレクトする。"""
		return reverse("PBSystem:bank_account_data_list")


class CustomerDeleteView(DeleteView, LoginRequiredMixin):
	template_name = "PBSystem/customerDeletion.html"
	model = CustomerList
	def get_success_url(self):
		return reverse("PBSystem:go-to-customerlist")


















