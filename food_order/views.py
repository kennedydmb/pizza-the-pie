from django.shortcuts import render
from .models import Food_order

# Create your views here.
def all_food_orders(request):
    """
    This will return all the food order items in the database
    """
    food_orders=Food_order.objects.all()
    return render(request, "food_order.html", {"food_orders":food_orders})
    
    
