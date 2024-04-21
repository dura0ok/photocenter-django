from django.urls import path

from queries.views import first_query, second_query

urlpatterns = [
    path('1', first_query),
    path('2', second_query),
]
