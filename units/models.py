"""Units models."""

# Django
from django.db import models

class BlockedDay(models.Model):
    """BlockedDays model."""
    # one to one field relation with `listings.BookingInfo`
    booking_info = models.OneToOneField(
        'listings.BookingInfo',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='blocked_day'
    )

    # blocked day field
    blocked_day = models.DateField(
        'Blocked day',
    )

    def __str__(self):
        """Return listing.__str__ and blocked_day."""
        return f'{self.booking_info} ({self.blocked_day})'