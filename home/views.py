from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Displays the home.html page
    """
    return (render(request, "home.html"))
