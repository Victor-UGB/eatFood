from rest_framework import serializers
from .models import FoodItem, FoodCategory
from vendors.models import FoodVendor
from vendors.serializers import VendorSerializer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ("category_name","category_tagline")


class FoodItemSerializer(serializers.ModelSerializer):
    # category = FoodCategorySerializer(read_only=True)
    # fooditem_vendor = VendorSerializer(many=True, read_only=True)

    class Meta:
        model = FoodItem
        fields = ("fooditem_name", "category", "fooditem_description", "fooditem_price", "fooditem_vendor")


class CreateFoodItemSerializer(serializers.ModelSerializer):
    category= serializers.SlugRelatedField(many=True, slug_field="category_name", queryset=FoodCategory.objects.all())
    # fooditem_vendor = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = FoodItem
        fields = ("fooditem_name", "category", "fooditem_description",
                "fooditem_price")
        
    # Create method
    def create():
        pass

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
