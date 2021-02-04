"""
	PBSystem application
	admin用の設定

	File name: admin.py
	Date: Jan 11, 2021
	Written by Nobuharu Shimazu
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import CustomerList,BankAccounts,Banks,UserType,User,BankAccountData


admin.site.register(CustomerList)
admin.site.register(BankAccounts)
admin.site.register(Banks)
admin.site.register(UserType)
admin.site.register(BankAccountData)


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',"short_name","email","password1","password2")


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('short_name', 'user_type', "email")}),
        (_('Permissions'), {'fields': ( 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', "short_name", "email", 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email', 'username', 'short_name')
    ordering = ('email',)


admin.site.register(User, MyUserAdmin)
