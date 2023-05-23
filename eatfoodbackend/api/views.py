from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
# from .models import FoodItem, FoodCategory
# from .serializers import FoodItemSerializer, FoodCategorySerializer
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@api_view(["GET"])
def home(request):
    return Response({
        "data": " Hello From Django Backend"
    })

# class FoodItemView(generics.ListAPIView):
#     queryset = FoodItem.objects.all()
#     serializer_class = FoodItemSerializer

# class FoodCategoryView(generics.ListAPIView):
#     queryset = FoodCategory.objects.all()
#     serializer_class = FoodCategorySerializer

@api_view(["GET", "POST"])
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=str(username), password=str(password))
        print(username)
        print(user)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return Response({'Message': 'Login Successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'Login Failed'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Message': 'Username and Password Required'} )