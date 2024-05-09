from django.urls import path
from .views import *

unused()

n = 10
urlpatterns = []

for i in range(1, n + 1):
    handler = getattr(locals()[f"Query{i}Handler"], 'as_view')
    urlpatterns.append(path(str(i), handler()))
