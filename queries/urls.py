from django.urls import path

from queries.views import *

urlpatterns = [
    path('1', Query1Handler.as_view()),
    path('2', Query2Handler.as_view()),
    path('3', get_special_orders_type_by_outlets),
    path('4', get_special_orders_revenue),
    path('5', get_prints_by_outlet),
]
