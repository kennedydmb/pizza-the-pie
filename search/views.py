from django.shortcuts import render
from courses.models import Course

# View to search the courses using user input
def do_search(request):
    courses = Course.objects.filter(name__icontains=request.GET['q'])
    return render(request, "courses.html", {"courses": courses})
    
