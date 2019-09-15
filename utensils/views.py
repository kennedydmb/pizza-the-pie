from django.shortcuts import render
from .models import Utensil

# Create your views here.
def all_utensils(request):
    """
    This will return all the utensils in the database
    """
    utensils=Utensil.objects.all()
    return render(request, "utensils.html", {"utensils":utensils})
    
def utensils_home(request):
    
    return render(request, "utensils_home.html")
    
    
