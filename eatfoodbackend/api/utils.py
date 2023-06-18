from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def rate_food_item(request_item, request_user, request_rating):
    
    item = get_food_item(request_item)  # Get food to rate
    user = get_user(request_user)  # Get User who is trying to rate
    rating = item.fooditem_rating  # Get rating
    # Get Vendor 
    new_rating = request_rating + rating // 2  # Calculate food rating (Average)
    item.fooditem_rating = new_rating # Set new rating on food_item
    item.save(update_fields=["fooditem_rating"])
    return (item.fooditem_rating)

    # if food_item in voter.food_history:
    #     pass
        
    # else:
    #     pass

def order_food(request_list, request_user):
    # Get order list
    # Seperate items in list
    # Disburse order request to vendor WABA
    # GeoLocate active dispatchers
    # Add a dispatcher to same whatsapp group by proximity with item vendor and eatfood bot
    # if items are along different routes then each route will have a dispatcher to deliver to a particular checkpoint
    # Geolocate closest dispatcher at checkpoint to make final dilery or have last dispatcher deliver items to customer
    
    pass

def create_food_item(fooditem_name, category, fooditem_description, fooditem_price, fooditem_vendor):
    pass


def get_food_item(request_item):
    item = FoodItem.objects.filter(id= request_item)

    if item.exists():
        return item[0]
    else:
        return None


def get_user(request_user):
    user = User.objects.filter(id= request_user)

    if user.exists():
        return user[0]
    else:
        return None
    
