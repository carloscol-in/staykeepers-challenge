"""Units admin."""

# Django
from django.contrib import admin

from .models import BlockedDay

class BlockedDaysAdmin(admin.ModelAdmin):
    """BlockedDay model admin."""
    pass
admin.site.register(BlockedDay, BlockedDaysAdmin)