from .utils import convert_string_to_variable_name as s2v

class ExtraContextMixin:
    """Add the model meta and model fields as objects to the context.

    Ignores the primary key and fields that are not editable.
    """

    def _get_model_context(self, model, context, context_meta, context_fields):
        # Assign the object's meta to a context variable.
        context[context_meta] = model._meta
        # Assign the object's fields to a context variable.
        context[context_fields] = []
        if hasattr(self,'fields') and not hasattr(self,'form_class'):
            fields = tuple(self.model._meta.get_field(x) for x in self.fields)
        else:
            fields = self.model._meta.get_fields()

        for fld in fields:
            if fld.editable and not fld.primary_key:
                context[context_fields].append(fld)

        return context

    def get_model_context(self, model, context):
        """Add context for a model's meta and fields to the context variable.

        model   -- A concrete model to be used in a template.
        context -- The context dictionary being passed to the template.

        Adds the model's meta and fields to the context dictionary, then returns
        the context dictionary.

        Typically, get_model_context() should be called as part of
        get_context_data() in order to get access to the _meta property of a
        the model passed. This is particuarly useful if more than one model will
        be used in the template (such as one that uses nested forms).
        """

        # If the model passed is self.model, create the generic "object" meta
        # and fields context items as well.
        if model == self.model:
            context_meta = "object_meta"
            context_fields = "object_fields"
            context = self._get_model_context(
                model,
                context,
                context_meta,
                context_fields
            )

        # Create the names for the context meta and fields objects
        context_meta = s2v(model._meta.model_name) + "_meta"
        context_fields = s2v(model._meta.model_name) + "_fields"

        # Get the context items.
        context = self._get_model_context(model,context,context_meta,context_fields)
        return context

    def get_context_data(self, **kwargs):

        # Get the context as normal.
        context = super().get_context_data(**kwargs)

        # Add context for model._meta and model._meta.fields
        context = self.get_model_context(self.model, context)

        # Do the same for any extra models that will be displayed as part of
        # this view.
        if hasattr(self, 'extra_models'):
            for model in self.extra_models.values():
                context = self.get_model_context(model, context)

        return context
