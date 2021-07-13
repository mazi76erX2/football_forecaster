from typing import Dict

from django.shortcuts import get_object_or_404
from django.db.models import QuerySet

from rest_framework.mixins import ListModelMixin


class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self: ListModelMixin) -> QuerySet:
        queryset: QuerySet = self.get_queryset()             # Get the base queryset
        queryset: QuerySet = self.filter_queryset(queryset)  # Apply any filter backends
        filter: Dict[None] = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj: QuerySet = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj