from django.conf.urls import url, include
from .views import course_review, add_review

urlpatterns = [      
    url(r'^course_review/(?P<id>\d+)', course_review, name='course_review'),
    url(r'^add_review/(?P<id>\d+)', add_review, name='add_review'),  
] 