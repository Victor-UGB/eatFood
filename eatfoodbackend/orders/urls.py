from .views import *
from django.urls import path

urlpatterns = [
    path('', order, name=""),
    path('processing', order_processing, name="")
]
