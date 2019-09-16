from django.conf.urls import url, include
from .views import all_courses

urlpatterns = [
    
    url(r'^$', all_courses, name='courses'),
    
]