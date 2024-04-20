from django.urls import path

from queries.views import first_query

urlpatterns = [
    path('1', first_query),
]
