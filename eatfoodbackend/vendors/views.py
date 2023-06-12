from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from .models import FoodVendor
from api.models import FoodCategory, FoodItem
from .serializers import *
from django.core import serializers as sr

# Create your views here.

@api_view(["GET"])
def home(request):
    return Response({'message': "Hello from Vendor app"})

class VendorsView(generics.ListAPIView):
    queryset = FoodVendor.objects.all()
    food_category_queryset = FoodCategory.objects.all()
    serializer_class = VendorSerializer
    

@api_view(["GET"])
def vendorsfulldetails(request):
    queryset = FoodVendor.objects.all()
    vendor_serializer_class = VendorSerializer
    category_serializer_class = FoodCategorySerializer
    # food_item_serializer_class = FoodItemSerializer
    

    # initialize empty list to store new list 
    new_queryset =[]

    for i in queryset:
        print(type(i), "loop")
        #get food categories where i is a member of category vendors
        vendor = FoodVendor.objects.filter(id=i.pk)
        vendor_category = i.vendor_catergories.all()

        #serialize querysets
        vendor_serialized = vendor_serializer_class(vendor, many=True).data[0]
        vendor_category_serialized = category_serializer_class(vendor_category, many=True).data

        # append to new _queryset
        new_queryset.append({'vendor':vendor_serialized, 'vendor_categories': vendor_category_serialized})

    return Response({'data' : new_queryset})

