from django.db import models

# Create your models here.
    
class FoodVendor(models.Model):
    user = models.CharField(max_length=200, default="victor") # Temporary entry to relate users and vendors table
    name = models.CharField(max_length=50, unique=True)
    tagline = models.CharField( max_length=200)
    vendor_rating = models.FloatField(default = 4.5)
    WA_contact = models.IntegerField(default= 9058166618)
    # subscriber = models.ManyToManyField()
    # vendor_logo = models.FileField(_(""), upload_to=None, max_length=100)
    # notification = 
    
    def __str__(self):
        return self.name
