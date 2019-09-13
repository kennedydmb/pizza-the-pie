from django.conf.urls import url, include
from .views import all_food_orders

urlpatterns = [
    url(r'^$', all_food_orders, name='food_orders'),
]