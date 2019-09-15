from django.shortcuts import render
from .models import Course

# Create your views here.
def all_courses(request):
    """
    This will return all the courses in the database
    """
    courses=Course.objects.all()
    return render(request, "courses.html", {"courses":courses})
    
def courses_home(request):
    """
    This will return all the courses in the database
    """
    return render(request, "courses_home.html")
    
    
