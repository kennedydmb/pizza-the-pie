from django.conf.urls import url, include
from .views import all_food_orders, food_ordering

urlpatterns = [
    url(r'^food_ordering', food_ordering, name='food_ordering'),
    url(r'^food_order', all_food_orders, name='food_orders'),
]