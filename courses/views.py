from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Course

# Create your views here.
def all_courses(request):
    """
    This will return all the courses in the database
    """
    courses_list=Course.objects.all()
    paginator = Paginator(courses_list, 6) # Show 6 courses per page

    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        courses = paginator.page(paginator.num_pages)
    return render(request, "courses.html", {"courses":courses})



