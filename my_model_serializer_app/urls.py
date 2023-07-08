from django.urls import path
from .views import *

urlpatterns = [
    path('contact_api_view/', ContactAPIView.as_view())
]
