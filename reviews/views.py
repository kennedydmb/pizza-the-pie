from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review
from courses.models import Course
from .forms import ReviewForm
import datetime


# Create your views here.
def course_review(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    reviews= Review.objects.filter(course = course_id)
    return render(request, "review.html", {"reviews":reviews, "course":course})
    
def add_review(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.course = course
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('course_review', args=(course_id)))

    return render(request, "review.html", {'course': course, 'form': form})