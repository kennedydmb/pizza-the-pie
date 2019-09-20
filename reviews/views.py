  
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
from django.conf import settings
from django.utils import timezone
from courses.models import Course

import datetime


# Create your views here.
def course_review(request, course_id):
    """
    Gets the most recent 10 reviews for the course
    """
    course = get_object_or_404(Course, pk=course_id)
    reviews= Review.objects.filter(course = course_id).order_by('-pub_date')[:10]
    return render(request, "review.html", {"reviews":reviews, "course":course})
    
def add_review(request,course_id):
    """
    To display the review form to the user
    """
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.user_name = "hey"
        form.save()
    return render(request, "create_review.html", {'form': form})
    
    