from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from .utils import *

# Create your views here.

@api_view(["GET", "POST"])
def order(request):
    orders = Order.objects.all()
    print(orders)
    serializer_class = OrderSerializer

    return Response(serializer_class(orders, many=True).data)


# Process Order

@api_view(["GET", "POST"])
def order_processing(request):
    orders = Order.objects.all()
    list_of_processed_orders = []

    for i in orders:
        print(i.pk)
        process = process_order(i.pk)
        list_of_processed_orders.append(process)

    return Response({'data': list_of_processed_orders})