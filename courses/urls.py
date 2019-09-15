from django.conf.urls import url, include
from .views import all_courses, courses_home

urlpatterns = [
    
    url(r'^explore/$', courses_home, name='explore'),
    url(r'^courses/$', all_courses, name='courses'),
]