from django.shortcuts import render
from .models import Course

# Create your views here.
def all_courses(request):
    """
    This will return all the courses in the database
    """
    courses=Course.objects.all()
    paginator = Paginator(courses, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, "courses.html", {"courses":courses})

