from .models import *
from django.urls import reverse_lazy
from .apps import AccountsConfig

class AccountModelConstants:
    MODEL = Account
    FIELDS = [
        'name',
        'parent',
        'account_type',
    ]
    PK_URL_KWARG = MODEL._meta.verbose_name + "_pk"
    PATTERN_NAME = AccountsConfig.name + ":" + MODEL._meta.verbose_name + "-list"
    SUCCESS_URL = reverse_lazy(AccountsConfig.name + ":" + MODEL._meta.verbose_name + "-list")

class LedgerEntryModelConstants:
    MODEL = LedgerEntry
    FIELDS = [
        'date',
        'memo',
    ]
    PK_URL_KWARG = MODEL._meta.verbose_name + "_pk"
    PATTERN_NAME = AccountsConfig.name + ":" + MODEL._meta.verbose_name + "-list"
    SUCCESS_URL = reverse_lazy(AccountsConfig.name + ":" + MODEL._meta.verbose_name + "-list")

class LedgerSplitModelConstants:
    MODEL = LedgerSplit
    FIELDS = [
        'memo',
		'account',
		'amount',
		'parent'
    ]
    PK_URL_KWARG = MODEL._meta.verbose_name + "_pk"
    PATTERN_NAME = AccountsConfig.name + ":" + MODEL._meta.verbose_name + "-list"
    SUCCESS_URL = reverse_lazy(AccountsConfig.name + ":" + MODEL._meta.verbose_name + "-list")
