from django.db import models
from vendors.models import FoodVendor
from api.models import FoodItem

# Create your models here.

class Order(models.Model):
    item = models.ForeignKey(FoodItem, related_name="order", on_delete=models.CASCADE)
    # vendor = models.ForeignKey(FoodVendor, related_name="vendor", on_delete=models.CASCADE)
    # user = ""
    date_created =  models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.item) + " order" + str(self.pk)