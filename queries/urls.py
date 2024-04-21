from django.urls import path

from queries.views import *

urlpatterns = [
    path('1', get_list_total_points_photo_orders_intake),
    path('2', get_orders_info_by_outlets),
    path('3', get_special_orders_type_by_outlets),
    path('4', get_special_orders_revenue),
]
