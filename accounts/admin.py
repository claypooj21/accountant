from django.contrib import admin
from . models import *
from utilities import TrackingMixinAdmin

class AccountAdmin(TrackingMixinAdmin):
	pass

class LedgerEntryAdmin(TrackingMixinAdmin):
	pass

class LedgerSplitAdmin(TrackingMixinAdmin):
	pass

admin.site.register(Account, AccountAdmin)
admin.site.register(LedgerEntry, LedgerEntryAdmin)
admin.site.register(LedgerSplit, LedgerSplitAdmin)