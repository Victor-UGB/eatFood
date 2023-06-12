from django.urls import path
from .views import *

urlpatterns = [
    path("", home , name=""),
    path("food_category", FoodCategoryView.as_view()),
    path("food_item_sht", FoodItemView.as_view()),
    path("food_item", food_item),
    path("login", login_view),
    path("register", register),
]
