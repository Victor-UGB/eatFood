from django.db import models
from django.contrib.auth.models import AbstractUser
from vendors.models import FoodVendor
from django.utils import timezone
import time
import datetime

# Create your models here.

# class User(AbstractUser):
#     pass


class FoodCategory(models.Model):
    category_name = models.CharField( max_length=50, unique=True, default="")
    category_tagline = models.CharField( max_length=300)
    category_vendors = models.ManyToManyField(FoodVendor, related_name= "vendor_catergories")

    def __str__(self):
        return self.category_name    

class FoodItem(models.Model):
    fooditem_name = models.CharField(max_length=50, default="Food Item")
    category = models.ManyToManyField(FoodCategory, related_name = "category_food_items")
    fooditem_description = models.CharField(max_length=300, default="Food Description")
    fooditem_price = models.IntegerField(null=False, default=0)
    fooditem_rating = models.FloatField(default=4.5)
    fooditem_vendor = models.ForeignKey(FoodVendor, related_name = "food_items", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fooditem_name
    
# Create Rating Class to rate fooditems