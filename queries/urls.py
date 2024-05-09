from django.urls import path
from .views import *

n = 8
urlpatterns = []

for i in range(1, n+1):
    handler = getattr(locals()[f"Query{i}Handler"], 'as_view')
    urlpatterns.append(path(str(i), handler()))
