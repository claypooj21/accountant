from django.views.generic import DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from utilities import ExtraContextMixin, TrackingCreateView, TrackingUpdateView
from .model_constants import *

#===============================================================================
#  ACCOUNT VIEWS
#===============================================================================
class AccountListView(ExtraContextMixin, LoginRequiredMixin, ListView):
    model = AccountModelConstants.MODEL

class AccountCreateView(ExtraContextMixin, LoginRequiredMixin, TrackingCreateView):
    model = AccountModelConstants.MODEL
    fields = AccountModelConstants.FIELDS

class AccountUpdateView(ExtraContextMixin, LoginRequiredMixin, TrackingUpdateView):
    model = AccountModelConstants.MODEL
    fields = AccountModelConstants.FIELDS
    pk_url_kwarg = AccountModelConstants.PK_URL_KWARG

class AccountDetailView(ExtraContextMixin, LoginRequiredMixin, DetailView):
    model = AccountModelConstants.MODEL
    fields = AccountModelConstants.FIELDS
    pk_url_kwarg = AccountModelConstants.PK_URL_KWARG

class AccountDeleteView(ExtraContextMixin, LoginRequiredMixin, DeleteView):
    model = AccountModelConstants.MODEL
    pk_url_kwarg = AccountModelConstants.PK_URL_KWARG
    success_url = AccountModelConstants.SUCCESS_URL


#===============================================================================
#  LEDGER ENTRY VIEWS
#===============================================================================
class LedgerEntryListView(ExtraContextMixin, LoginRequiredMixin, ListView):
    model = LedgerEntryModelConstants.MODEL

class LedgerEntryCreateView(ExtraContextMixin, LoginRequiredMixin, TrackingCreateView):
    model = LedgerEntryModelConstants.MODEL
    fields = LedgerEntryModelConstants.FIELDS

class LedgerEntryUpdateView(ExtraContextMixin, LoginRequiredMixin, TrackingUpdateView):
    model = LedgerEntryModelConstants.MODEL
    fields = LedgerEntryModelConstants.FIELDS
    pk_url_kwarg = LedgerEntryModelConstants.PK_URL_KWARG

class LedgerEntryDetailView(ExtraContextMixin, LoginRequiredMixin, DetailView):
    model = LedgerEntryModelConstants.MODEL
    fields = LedgerEntryModelConstants.FIELDS
    pk_url_kwarg = LedgerEntryModelConstants.PK_URL_KWARG

class LedgerEntryDeleteView(ExtraContextMixin, LoginRequiredMixin, DeleteView):
    model = LedgerEntryModelConstants.MODEL
    pk_url_kwarg = LedgerEntryModelConstants.PK_URL_KWARG
    success_url = LedgerEntryModelConstants.SUCCESS_URL


#===============================================================================
#  LEDGER SPLIT VIEWS
#===============================================================================
class LedgerSplitListView(ExtraContextMixin, LoginRequiredMixin, ListView):
    model = LedgerSplitModelConstants.MODEL

class LedgerSplitCreateView(ExtraContextMixin, LoginRequiredMixin, TrackingCreateView):
    model = LedgerSplitModelConstants.MODEL
    fields = LedgerSplitModelConstants.FIELDS

class LedgerSplitUpdateView(ExtraContextMixin, LoginRequiredMixin, TrackingUpdateView):
    model = LedgerSplitModelConstants.MODEL
    fields = LedgerSplitModelConstants.FIELDS
    pk_url_kwarg = LedgerSplitModelConstants.PK_URL_KWARG

class LedgerSplitDetailView(ExtraContextMixin, LoginRequiredMixin, DetailView):
    model = LedgerSplitModelConstants.MODEL
    fields = LedgerSplitModelConstants.FIELDS
    pk_url_kwarg = LedgerSplitModelConstants.PK_URL_KWARG

class LedgerSplitDeleteView(ExtraContextMixin, LoginRequiredMixin, DeleteView):
    model = LedgerSplitModelConstants.MODEL
    pk_url_kwarg = LedgerSplitModelConstants.PK_URL_KWARG
    success_url = LedgerSplitModelConstants.SUCCESS_URL