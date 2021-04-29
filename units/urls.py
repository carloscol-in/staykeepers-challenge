"""Units urls."""

# Django
from django.urls import path

# Views
from .views import ListUnitsAPIView

urlpatterns = [
    path('', ListUnitsAPIView.as_view(), name='list')
]