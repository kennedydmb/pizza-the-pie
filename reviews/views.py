  
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
    course = get_object_or_404(Course, pk=course_id)
    reviews= Review.objects.filter(course = course_id)
    return render(request, "review.html", {"reviews":reviews, "course":course})
    
def add_review(request, course_id):
    if request.method=="POST":
        review_form = ReviewForm(request.POST)
        
        if review_form.is_valid():
            review = review_form.save
            review.date = timezone.now()
            review.save()
            
        else:
            print(review_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        
        review_form = ReviewForm()
        
    
    return render(request, "review.html", {'review_form': review_form})
    
    