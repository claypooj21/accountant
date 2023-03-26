from django.db import models
from utilities import TrackingMixin
from djmoney.models.fields import MoneyField
from django.urls import reverse
from .apps import AccountsConfig

class Account(TrackingMixin, models.Model):

	# Account name
	name = models.CharField(
		max_length = 128, 
		blank = False
	)

	# Parent
	parent = models.ForeignKey(
		'self',
		blank = True,
		null = True, 
		on_delete=models.CASCADE
	)

	# Account Type Choices
	class AccountType(models.TextChoices):
		ASSETS = 'a', 'Assets'
		LIABILITIES = 'l', 'Liabilities'
		EQUITIES = 'e', 'Equities'
		REVENUES = 'r', 'Revenues'
		EXPENSES = 'x', 'Expenses'

	# Account type
	account_type = models.CharField(
		max_length = 1,
		choices = AccountType.choices,
		null = False,
		blank = False
	)

	def __str__(self):
		return self.name

	def is_placeholder(self):
		return Account.objects.filter(parent__pk = self.pk).count() > 0

	def get_absolute_url(self):
		return reverse(AccountsConfig.name + ':' + self._meta.model_name + '-detail', kwargs={self._meta.model_name + '_pk':self.pk})


class LedgerEntry(TrackingMixin, models.Model):
	
	class meta:
		verbose_name_plural = "ledger entries"

	# Date of the ledger entry
	date = models.DateTimeField(
		null = False, 
		blank = False
	)

	# Description of the transaction
	memo = models.TextField(
		blank = False, 
		null = False
	)

	def __str__(self):
		return str(self.date) + ": " + memo

	def get_absolute_url(self):
		return reverse(AccountsConfig.name + ':' + self._meta.model_name + '-detail', kwargs={self._meta.model_name + '_pk':self.pk})


class LedgerSplit(TrackingMixin, models.Model):
	
	# Description of the transaction
	memo = models.TextField(
		blank = False, 
		null = False
	)

	# Account this line applies to
	account = models.ForeignKey(
		Account,
		null = True,
		on_delete=models.SET_NULL,
		limit_choices_to = {'is_placeholder': False}
	)

	# Amount credited or debited
	amount = MoneyField(
		max_digits=19, 
		decimal_places=2, 
		default_currency='USD'
	)

	# The general ledger entry this split is a part of
	parent = models.ForeignKey(
		LedgerEntry, 
		null = False, 
		on_delete=models.CASCADE
	)

	def __str__(self):
		return self.account.name + ": " + str(amount)

	def get_absolute_url(self):
		return reverse(AccountsConfig.name + ':' + self._meta.model_name + '-detail', kwargs={self._meta.model_name + '_pk':self.pk})