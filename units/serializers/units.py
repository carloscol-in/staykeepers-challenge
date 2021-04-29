"""Units serializers."""

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from units.models import BlockedDay

class BlockedDaySerializer(serializers.ModelSerializer):
    """BlockedDay model serializer."""
    listing_type = serializers.SerializerMethodField()
    # title = serializers.SerializerMethodField()
    # country = serializers.SerializerMethodField()
    # city = serializers.SerializerMethodField()
    # price = serializers.SerializerMethodField()
    
    class Meta:
        model = BlockedDay
        fields = ['listing_type']

    def get_listing_type(self, obj):
        blocked_day = BlockedDay.objects.filter(blocked_day=obj)
        return blocked_day.booking_info.hotel_room_type.hotel.listing_type.capitalize()