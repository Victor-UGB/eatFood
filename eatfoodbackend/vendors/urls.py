from django.urls import path
from .views import *

urlpatterns = [
    path("hello", home , name=""),
    path("", VendorsView.as_view(), name=""),
    path("full", vendorsfulldetails)
]
