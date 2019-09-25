from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
from django.conf import settings
from django.utils import timezone
from courses.models import Course
from django.contrib.auth.models import User

import datetime


# Create your views here.
def course_review(request, id):
    """
    Gets the most recent 10 reviews for the course
    """
    course = get_object_or_404(Course, pk=id)
    reviews= Review.objects.filter(course = id).order_by('-pub_date')[:10]
    return render(request, "review.html", {"reviews":reviews, "course":course})
    
def add_review(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.course = course
            review.user_name = request.user
            form.save()
            courses = Course.objects.all()
        return redirect('courses')
    else:
        form=ReviewForm()
        return render(request, "create_review.html", {'course':course, 'form': form}) 