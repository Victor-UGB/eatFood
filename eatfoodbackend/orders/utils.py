from .models import *
from django.shortcuts import get_object_or_404

def process_order(order_id):
    # filter order 
    try:
        order = get_object_or_404(Order, id = order_id)
        item = get_object_or_404(FoodItem, id = order.item)
        vendor = get_object_or_404(FoodVendor, id = item.fooditem_vendor)
        contact = vendor.WA_contact
        vendor_profile = vendor.user

        return {'order': order,
                'item': item,
                'vendor': vendor,
                'contact': contact,
                'vendor_profile': vendor_profile
                }
    except :
        return {'error': 'Order does not exists'}

        # get item details
        # get order vendor
        # Send order request to vendor profile, whatsapp and gmail.

    # get user
        # Send processing confirmation message
    pass

