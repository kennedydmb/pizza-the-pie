from django.shortcuts import render, get_object_or_404
from .models import Review
from courses.models import Course

# Create your views here.
def course_review(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    reviews= Review.objects.filter(course = course_id)
    return render(request, "review.html", {"reviews":reviews, "course":course})