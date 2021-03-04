"""
PBSystem application
　データモデル

	Filename   models.py
	Date       2021/1/6
	Written by Nobuharu Shimazu
"""
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomerList(models.Model):
	"""
		customer_name: お客さんの名前
	"""
	customer_name = models.CharField(max_length=200)

	def __str__(self):
		return str(self.customer_name)




class BankAccounts(models.Model):
	"""
		#customer: お客さんの名前   from CustomerList
		#match: 二人の入力した情報があっているかいないか
		#wether_complete: コンプリートにされているかされてないか

	"""
	# foreignkey
	customer = models.ForeignKey(CustomerList,on_delete=models.CASCADE)
	
	match = models.BooleanField(default=False)
	wether_complete = models.BooleanField(default=False)

	def __str__(self):
		return str(self.customer) + " : " + str(self.match) + " : " + str(self.wether_complete)





class Banks(models.Model):
	"""
		bank_name_Viet: ベトナム語の銀行の名前
		bank_name_En: 英語の銀行の名前
	"""
	bank_name_Viet = models.CharField(max_length=200)
	bank_name_En = models.CharField(max_length=200)

	def __str__(self):
		return str(self.bank_name_En) + " (" + str(self.bank_name_Viet) + ")"



class UserType(models.Model):
	"""
		user_type: ユーザーのタイプ
	"""
	user_type = models.CharField(max_length=200)

	def __str__(self):
		return str(self.user_type)

from django.contrib.auth.models import PermissionsMixin, UserManager

class CustomUserManager(UserManager):
    """ユーザーマネージャー"""
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)        
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)




class User(AbstractBaseUser,PermissionsMixin):
	"""
		user: djangoのデータベースにあるユーザーテーブルに情報を足す
		user_type: ユーザーのタイプ
		short_name: ショートネーム
		modified: ユーザー情報が書き換えられた日付
		created: ユーザーが作られた日付
	"""
	# foreignkeys
	user_type = models.ForeignKey(UserType,on_delete=models.CASCADE,null=True,default=None,blank=True)
	email = models.EmailField(unique=True)
	username = models.CharField(unique=True,max_length=200)

	short_name = models.CharField(max_length=5)
	modified = models.DateTimeField(blank=True,null=True)
	date_joined = models.DateTimeField(default=timezone.now)
	objects = CustomUserManager()

	def modified(self):
		self.modified = timezone.now()
		self.save

	def __str__(self):
		return str(self.id) + str(self.short_name) + "   type: " + str(self.user_type)

	EMAIL_FIELD = "email"
	USERNAME_FIELD = "username"

	is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )




class BankAccountData(models.Model):
	"""
		custome 
		banks: ベトナムの銀行のベトナム語バージョンと英語バージョン
		user_info: ユーザーの情報
		bank_branch_name: 銀行の支店名
		bank_address: 銀行の住所
		banker_1: 銀行側人１
		banker_2: 銀行側人２
		reg_date: 情報を入力した日付
		bank_account: 銀行口座番号
		bank_account_holder: 名義人
	"""
	# foreignkeys
	bank_accounts = models.ForeignKey(BankAccounts,on_delete=models.CASCADE)
	banks = models.ForeignKey(Banks,on_delete=models.CASCADE)
	user_info = models.ForeignKey(User,on_delete=models.CASCADE)

	bank_branch_name = models.CharField(max_length=200)
	bank_address = models.TextField()
	banker_1 = models.CharField(blank=False,null=False,max_length=200)
	banker_2 = models.CharField(blank=True,null=True,max_length=200)
	reg_date = models.DateTimeField(default=timezone.now)
	date = models.DateTimeField(blank=False, null=False, default=timezone.now)
	bank_account = models.CharField(max_length=200)
	bank_account_holder = models.CharField(max_length=200)







