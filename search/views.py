from django.shortcuts import render
from courses.models import Course

# Create your views here.
def do_search(request):
    courses = Course.objects.filter(name__icontains=request.GET['q'])
    return render(request, "courses.html", {"courses": courses})