from django.urls import path

from queries.views import *

urlpatterns = [
    path('1', Query1Handler.as_view()),
    path('2', Query2Handler.as_view()),
    path('3', Query3Handler.as_view()),
    path('4', Query4Handler.as_view()),
    path('5', Query5Handler.as_view()),
]
