from django.shortcuts import render
from courses.models import Course

# Create your views here.
def price_ascend(request):
    courses=Course.objects.order_by('price')
    return render(request, "courses.html", {"courses": courses})
    
def price_descend(request):
    courses=Course.objects.order_by('-price')
    return render(request, "courses.html", {"courses": courses})
    
def name_ascend(request):
    courses=Course.objects.order_by('name')
    return render(request, "courses.html", {"courses": courses})
    
def name_descend(request):
    courses=Course.objects.order_by('-name')
    return render(request, "courses.html", {"courses": courses})
    