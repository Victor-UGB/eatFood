from django.db import models

# Create your models here.
    
class FoodVendor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField( max_length=200)
    vendor_rating = models.FloatField(default = 4.5)
    # vendor_logo = models.FileField(_(""), upload_to=None, max_length=100)
    
    def __str__(self):
        return self.name