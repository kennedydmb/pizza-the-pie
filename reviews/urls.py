from django.conf.urls import url, include
from .views import course_review

urlpatterns = [
    
    url(r'^course_review/(?P<course_id>\d+)', course_review, name='course_review'),
    
]


