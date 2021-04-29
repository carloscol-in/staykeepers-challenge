"""Units views."""

# Django REST Framework
from rest_framework.views import APIView
from rest_framework import status, filters
from rest_framework.response import Response

# Models
from listings.models import BookingInfo

# Serializers
from listings.serializers import BookingInfoSerializer

class ListUnitsAPIView(APIView):
    """List units API view.
    
    This API will list units from BookingInfo model where certain conditions are
    met. This conditions are passed on the HTTP GET parameters:
        + check_in (datetime): When customer expects to arrive
        + check_out (datetime): When customer expects to leave
        + max_price (int, float): Customer's max budget for the place
    """

    def get(self, request, *args, **kwargs):
        """Handle HTTP GET requests on this API view."""
        # Bring all BookingInfo objects, exclude the ones where blocked_day
        # is greater than check-in and lower than check-out, then, exclude the
        # listings where price is greater than or equal to max_price.
        filtered_bookings = BookingInfo.objects.exclude(
            blocked_day__blocked_day__gt=request.GET['check_in'],
            blocked_day__blocked_day__lt=request.GET['check_out']
        ).exclude(
            price__gte=200
        ).order_by(
            'price'
        )

        # import pdb; pdb.set_trace()
        # Get serialized object
        # for fil_booking in filtered_bookings:
        serializer = BookingInfoSerializer(
            data=filtered_bookings,
            many=True
        )
        # filter_backends = [filters.OrderingFilter]
        # ordering_fields = ['price']
        # ordering = ['price']
        # Check if serializer is valid, otherwise, raise exception
        serializer.is_valid()
        # Append data to data object on items key
        data = {
            'items': serializer.data
        }

        return Response(data)