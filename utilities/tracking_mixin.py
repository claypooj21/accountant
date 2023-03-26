from django.db import models
from .utils import get_sentinel_user
from django.conf import settings
from django.contrib import admin
from django.views.generic import CreateView, UpdateView


class TrackingMixin(models.Model):

    class Meta:
        abstract = True

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET(get_sentinel_user),
        related_name = "%(class)s_created_by",
        editable = False
    )

    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET(get_sentinel_user),
        related_name = '%(class)s_last_modified_by',
        editable = False
    )

    datetime_created = models.DateTimeField(auto_now_add = True)

    datetime_modified = models.DateTimeField(auto_now = True)

    datetime_removed = models.DateTimeField(
        blank = True,
        null = True,
        editable = False
    )

    def is_active(self):
        return False if self.datetime_removed else True


class TrackingMixinAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_by',
        'last_modified_by',
        'datetime_created',
        'datetime_modified',
        'datetime_removed',
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.last_modified_by = request.user
        super().save_model(request, obj, form, change)


class BaseTrackingViewMixin:
    def update_last_modified_by(self, form):
        form.instance.last_modified_by = self.request.user
        return form

    def form_valid(self, form):
        """If the form is valid, update user data."""
        form = self.update_last_modified_by(form)
        return super().form_valid(form)

class TrackingUpdateView(BaseTrackingViewMixin, UpdateView):
    pass

class TrackingCreateView(BaseTrackingViewMixin, CreateView):

    def update_created_by(self, form):
        form.instance.created_by = self.request.user
        return form

    def form_valid(self, form):
        """If the form is valid, add user data."""
        form = self.update_created_by(form)
        return super().form_valid(form)
