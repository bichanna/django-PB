# Generated by Django 3.0.2 on 2021-02-18 01:35

import PBSystem.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name_Viet', models.CharField(max_length=200)),
                ('bank_name_En', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('short_name', models.CharField(max_length=5)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('user_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='PBSystem.UserType')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', PBSystem.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BankAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.BooleanField(default=False)),
                ('wether_complete', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PBSystem.CustomerList')),
            ],
        ),
        migrations.CreateModel(
            name='BankAccountData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_branch_name', models.CharField(max_length=200)),
                ('bank_address', models.TextField()),
                ('banker_1', models.CharField(max_length=200)),
                ('banker_2', models.CharField(blank=True, max_length=200, null=True)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('bank_account', models.CharField(max_length=200)),
                ('bank_account_holder', models.CharField(max_length=200)),
                ('bank_accounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PBSystem.BankAccounts')),
                ('banks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PBSystem.Banks')),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
