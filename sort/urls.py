from django.conf.urls import url
from .views import price_ascend, price_descend

urlpatterns = [
    url(r'^price_ascend/', price_ascend, name='price_ascend'),
    url(r'^price_descend/', price_descend, name='price_descend'),
    ]