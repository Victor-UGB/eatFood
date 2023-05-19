from django.urls import path
from .views import *

urlpatterns = [
    path("", home , name=""),
    path("vendors", VendorsView.as_view(), name=""),
    path("login", login_view)
]
