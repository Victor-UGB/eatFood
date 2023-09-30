from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from .models import FoodVendor
from api.models import *
from .serializers import *
from django.core import serializers as sr
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


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


# Create new vendor
@api_view(["POST"])
def create_vendor(request):
    print(User.objects.all())
    # serializer = VendorSerializer
    if request.method == "POST":
        # Check if user exist in database
        user = User.objects.filter(username = request.data['username'])
        # user = User.objects.filter(username = "victor")
        print(user)

        if user.exists(): # If user exists and has not created a vendor 
            name  = request.data["name"]
            tagline = request.data["tagline"]
            vendor_rating = 4.5
            # vendor_contact_number = 09012234456
            # vendor_email = 

            # Create new vendor instamce or grant vendor priviledges
            new_vendor = FoodVendor(user = user, name = name, tagline = tagline, vendor_rating = vendor_rating)
            new_vendor.save()
            print(User.objects.all())
            return Response({"Success": "Vendor has been created successfully"}, status=status.HTTP_201_CREATED)
        
        return Response({"User not found": "You need to be a user to become a vendor. Create account now or Login"}, status=status.HTTP_404_NOT_FOUND)
        
    return Response({"Bad Request": "Post request expected"}, status=status.HTTP_400_BAD_REQUEST)
    # pass

# Create Food item
@api_view(["POST", "GET"])
def create_fooditem(request):
    print(FoodItem.objects.all())
    user = request.user
    
    # Check request method
    if request.method == "POST":
        # print(request.user)
        try:
            vendor = get_object_or_404(
                FoodVendor, user=user)  # Get vendor profile
            print(vendor.user)
        except ValueError :
            return Response({"error": "User is not a vendor"})
        
        vendor_fooditems = FoodItem.objects.filter(fooditem_vendor = vendor) # Return queryset of fooditems created vendor 
        print(vendor_fooditems)
        
        # Create food item
        new_fooditem = FoodItem(
            fooditem_name = request.data["fooditem_name"],
            category = 2, #revisit issue
            fooditem_description = request.data["fooditem_description"],
            fooditem_price = request.data["fooditem_price"],
            fooditem_rating = 4.5,
            fooditem_vendor = vendor
            )
        
        new_fooditem.save()

        return Response({"message": "Food item created successfully"})

    else:
        print(request.user)
        return Response({"message" : "Item returned"})






