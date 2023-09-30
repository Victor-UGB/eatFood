from django.urls import path
from .views import *

urlpatterns = [
    path("hello", home , name=""),
    path("", VendorsView.as_view(), name=""),
    path("full", vendorsfulldetails),
    path("new_vendor", create_vendor),
    path('new_fooditem', create_fooditem)
]
