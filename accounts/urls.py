"""accounts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import *
from .apps import AccountsConfig

app_name = AccountsConfig.name

# ==============================================================================
# LEDGER SPLITS
# ==============================================================================

ledger_split_detail_paths = [
    path('delete/', LedgerSplitDeleteView.as_view(extra_context = {'title_block':' | Delete Ledger Split'}), name = 'ledgersplit-delete'),
    path('update/', LedgerSplitUpdateView.as_view(extra_context = {'title_block':' | Update Ledger Split'}), name = 'ledgersplit-update'),
    path('', LedgerSplitDetailView.as_view(extra_context = {'title_block':' | Ledger Split Details'}), name = 'ledgersplit-detail'),
]

ledger_split_paths = [
	path('', LedgerSplitListView.as_view(extra_context = {'title_block':' | Ledger Splits'}), name = 'ledgersplit-list'),
    path('create/', LedgerSplitCreateView.as_view(extra_context = {'title_block':' | New Ledger Split'}), name = 'ledgersplit-create'),
    path('<int:ledgersplit_pk>/', include(ledger_split_detail_paths)),
]


# ==============================================================================
# LEDGER ENTRIES
# ==============================================================================

ledger_entry_detail_paths = [
    path('ledgersplits/', include(ledger_split_paths)),
    path('delete/', LedgerEntryDeleteView.as_view(extra_context = {'title_block':' | Delete Ledger Entry'}), name = 'ledgerentry-delete'),
    path('update/', LedgerEntryUpdateView.as_view(extra_context = {'title_block':' | Update Ledger Entry'}), name = 'ledgerentry-update'),
    path('', LedgerEntryDetailView.as_view(extra_context = {'title_block':' | Ledger Entry Details'}), name = 'ledgerentry-detail'),
]

ledger_entry_paths = [
	path('', LedgerEntryListView.as_view(extra_context = {'title_block':' | Ledger Entries'}), name = 'ledgerentry-list'),
    path('create/', LedgerEntryCreateView.as_view(extra_context = {'title_block':' | New Ledger Entry'}), name = 'ledgerentry-create'),
    path('<int:ledgerentry_pk>/', include(ledger_entry_detail_paths)),
]



# ==============================================================================
# ACCOUNTS
# ==============================================================================

account_detail_paths = [
    path('ledger/', include(ledger_entry_paths)),
    path('delete/', AccountDeleteView.as_view(extra_context = {'title_block':' | Delete Account'}), name = 'account-delete'),
    path('update/', AccountUpdateView.as_view(extra_context = {'title_block':' | Update Account'}), name = 'account-update'),
    path('', AccountDetailView.as_view(extra_context = {'title_block':' | Account Details'}), name = 'account-detail'),
]

account_paths = [
	path('', AccountListView.as_view(extra_context = {'title_block':' | Accounts'}), name = 'account-list'),
    path('create/', AccountCreateView.as_view(extra_context = {'title_block':' | New Account'}), name = 'account-create'),
    path('<int:account_pk>/', include(account_detail_paths)),
]

# ==============================================================================
# MAIN
# ==============================================================================

urlpatterns = [
    path('', include(account_paths)),
]
