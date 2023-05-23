# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import generics, status
# from rest_framework.decorators import api_view
# from .models import FoodVendor
# from .serializers import VendorSerializer

# # Create your views here.

# @api_view(["GET"])
# def home(request):
#     return Response({'message': "Hello from Vendor app"})

# class VendorsView(generics.ListAPIView):
#     queryset = FoodVendor.objects.all()
#     serializer_class = VendorSerializer
    
