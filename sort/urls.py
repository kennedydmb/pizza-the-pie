from django.conf.urls import url
from .views import price_ascend, price_descend, name_ascend, name_descend

urlpatterns = [
    url(r'^price_ascend/', price_ascend, name='price_ascend'),
    url(r'^price_descend/', price_descend, name='price_descend'),
    url(r'^name_ascend/', name_ascend, name='name_ascend'),
    url(r'^name_descend/', name_descend, name='name_descend'),
    ]