"""BookingInfo serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from listings.models import BookingInfo

class BookingInfoSerializer(serializers.Serializer):
    """BookingInfo model serializer."""
    listing_type = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = BookingInfo
        fields = '__all__'

    # Properties are different for apartments and hotels.
    # Apartments have `listing`, hotels have `hotel_room_type`.
    def get_listing_type(self, obj):
        """Get the `listing_type` from obj, which is a
        `BookingInfo` instance."""
        if (obj.listing):
            listing_type = obj.listing.listing_type
        elif (obj.hotel_room_type):
            listing_type = obj.hotel_room_type.hotel.listing_type
        listing_type = listing_type.capitalize()
        return f'{listing_type}'

    def get_title(self, obj):
        """Get the `title` from obj, which is a `BookingInfo`
        instance."""
        if (obj.listing):
            title = obj.listing.title
        elif (obj.hotel_room_type):
            title = obj.hotel_room_type.hotel.title
        return f'{title}'

    def get_country(self, obj):
        """Get the `country` from obj, which is a `BookingInfo`
        instance."""
        if (obj.listing):
            country = obj.listing.country
        elif (obj.hotel_room_type):
            country = obj.hotel_room_type.hotel.country
        return f'{country}'

    def get_city(self, obj):
        """Get the `city` from obj, which is a `BookingInfo`
        instance."""
        if (obj.listing):
            city = obj.listing.city
        elif (obj.hotel_room_type):
            city = obj.hotel_room_type.hotel.city
        return f'{city}'

    def get_price(self, obj):
        """Get the `country` from obj, which is a `BookingInfo`
        instance."""
        return f'{int(obj.price)}'