from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     pass

class FoodCategory(models.Model):
    category_name = models.CharField( max_length=50, unique=True)
    category_tagline = models.CharField( max_length=300)

    def __str__(self):
        return self.category_name
    
    
class FoodItem(models.Model):
    pass

class Vendor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField( max_length=200)
    food_categories = models.ManyToManyField(FoodCategory, related_name="category_vendors")
    # vendor_logo = models.FileField(_(""), upload_to=None, max_length=100)
    
    def __str__(self):
        return self.name
    