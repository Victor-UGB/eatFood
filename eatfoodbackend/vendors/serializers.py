from rest_framework import serializers
from .models import FoodVendor
from api.models import FoodCategory

class VendorSerializer(serializers.ModelSerializer):
    # vendor_food_categories = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=FoodCategory.objects.all())

    class Meta:
        model = FoodVendor
        fields = ("name", "tagline", "vendor_rating")

class VendorDetailsSerializer(serializers.Serializer):
    vendor = serializers.DictField()
    vendor_categories = serializers.DictField()

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= FoodCategory
        fields = ("category_name", "category_tagline", "category_vendors")
