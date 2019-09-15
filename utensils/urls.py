from django.conf.urls import url, include
from .views import all_utensils, utensils_home

urlpatterns = [
    
    url(r'^utensil/$', utensils_home, name='utensil'),
    url(r'^utensils/$', all_utensils, name='utensils'),
]