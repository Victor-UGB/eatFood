from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path("", home , name=""),
    path("food_category", FoodCategoryView.as_view()),
    path("food_item_sht", FoodItemView.as_view()),
    path("create_food_item", CreateFoodItem.as_view()),
    path("food_item", food_item),
    path("food_vendor", get_vendor),
    path("food_category", get_category),
    path("login", login_view),
    path("register", register),
]
