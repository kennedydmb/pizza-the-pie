from django.shortcuts import render
from .models import Course, Review

# Create your views here.
def all_courses(request):
    """
    This will return all the courses in the database
    """
    courses=Course.objects.all()
    reviews=Review.objects.all()
    return render(request, "courses.html", {"courses":courses, "reviews":reviews})

    
