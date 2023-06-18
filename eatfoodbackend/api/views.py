from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import FoodItem, FoodCategory
from vendors.serializers import VendorDetailsSerializer
from .serializers import *
from vendors.models import FoodVendor
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(["GET"])
def home(request):
    return Response({
        "data": " Hello From Django Backend"
    })

class FoodItemView(generics.ListAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class FoodCategoryView(generics.ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

# @method_decorator(csrf_exempt, name="dispatch")
class CreateFoodItem(APIView):
    serializers_class = CreateFoodItemSerializer
    query_set = FoodItem

    def post(self, request):
        ser = self.serializers_class(data=request.data)
        print(request.data)
        print(ser)
        if ser.is_valid():
            fooditem_name = ser.data.get("fooditem_price")
            category = ser.data.get("category")
            fooditem_description = ser.data.get("fooditem_description")
            fooditem_price = ser.data.get("fooditem_price")
            fooditem_vendor = ser.data.get("fooditem_vendor")
            i = get_object_or_404(FoodCategory, category_name = category[0])
            print(f"This {i.category_tagline}")
            print(f"{i.category_food_items.all()}")
            print(category)
            
            new_food_item = FoodItem()
            return Response({"data": "create food api functional"})
        return Response({"data": ser.errors})
    

@api_view(["GET", "POST"])
def get_category(request):
    serializer_class = FoodCategorySerializer

    if request.method == "POST":
        serialiized_data = serializer_class(data=request.data)
        if serialiized_data.is_valid():
            # get category from serialized data
            category = serialiized_data.data.get("category_name")
            # query for all food_items in category
            category = FoodCategory.objects.filter(category_name= category)
            food_items = category.category_food_item.all()

    elif request.method == "GET":
        id = request.GET.get("id")
        queryset = FoodCategory.objects.all()
        if id:
            pass
        
        return Response({"data": serializer_class(queryset, many=True).data})


@api_view(["GET", "POST"])
def get_vendor(request):
    serializer_class = VendorSerializer

    if request.method == "POST":
        serialized_data = serializer_class(data=request.data)
        if serialized_data.is_valid():
            vendor = serialized_data.data.get()

    elif request.method == "GET":
        id = request.GET.get("id")
        queryset = FoodVendor.objects.all()
        
        if id:
            pass

        return Response({"data": serializer_class(queryset, many=True).data})

@api_view(["GET", "POST"])
def food_item(request, *args, **kwargs):
    food_item_serializer = FoodItemSerializer
    serializer = food_item_serializer(data=request.data)
    
    #Create new food item
    if request.method == "POST":
        if serializer.is_valid():
            # fooditem_name = serializer.data.get("fooditem_name")
            # category = list(FoodCategory.objects.filter(id = serializer.data.get("category")) )
            # fooditem_description = serializer.data.get("fooditem_description")
            # fooditem_price  = serializer.data.get("fooditem_price")
            # fooditem_rating = 4.5
            # fooditem_vendor = FoodVendor.objects.filter(id = serializer.data.get("fooditem_vendor")) 

            return Response({"Message": "Created Successfully"})
        return Response({'Failed': "Params not valid"})
    
    #Get Food Item by query parameter
    elif request.method == "GET":
            id = request.GET.get("id")
            print(id)
            if id:
                try:
                    item = get_object_or_404(FoodItem, id=id)
                except item == None:
                    return Response({"Error": "Item does not exists"})
                
                item = food_item_serializer(item).data
                return Response(item, status=status.HTTP_200_OK)
            
            #Get all Food Items
            items = FoodItem.objects.all()
            return Response(food_item_serializer(items, many=True).data)
    
    #Handle Other Request types
    return Response({'Bad Request': "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

def order_food_item(request):
    serializer_class = "" #Food Item Serializer?

    if request.method == "POST":
        serialized_data = serializer_class(data=request.data)
        if serialized_data.is_valid():
            items = serialized_data.data.get()
            user = serialized_data.data.get()
            # Check if there is more than one item
            vendors = serialized_data.data.get()
            # Call the order food function




    
def user_logged_in(request):
    pass

@api_view(["GET", "POST"])
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=str(
            username), password=str(password))
        print(username)
        print(user)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return Response({'Message': 'Login Successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'Login Failed'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Message': 'Username and Password Required'})


@api_view(["GET", "POST"])
def register(request):
    serializer_class = UserSerializer
    users = User.objects.all()
    # form = NewUserForm
    if request.method == "POST":
        request_serialized = serializer_class(data=request.data)
        print(request_serialized)
        # form = form(request.data)
        if request_serialized.is_valid():
            # user=form.save()
            email = request_serialized.data.get("email")
            username = request_serialized.data.get("username")

            password = request_serialized.data.get("password")
            confirmation = request.data.get("password2")
            if password != confirmation:
                return Response({"Warning": "Passwords do not match"})
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                return Response({"Warning": "Username already exists"}, status=status.HTTP_409_CONFLICT)
            login(request, user)
            return Response({"Success": "User has been created successfully"})
            # if email not in users:
            #     username = request_serialized.data.get("username")
            #     if username != users:
            #         return Response({"Success": "User has been registered"}, status=status.HTTP_200_OK)
                
            # return Response({"Failed": "Email already associated with account"}, status=status.HTTP_409_CONFLICT)
        return Response({'Failed': "Params not valid"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        print(users)
        return Response({'Register': "Register as New Uer"}, status=status.HTTP_200_OK)

