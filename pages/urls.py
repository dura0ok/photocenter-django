from django.urls import path

from pages import views
from pages.views import LoginPageView, LogoutPageView, CreateOrder

urlpatterns = [
    path('', views.index, name='index'),
    path('login', LoginPageView.as_view(), name='login'),
    path('logout', LogoutPageView.as_view(), name='logout'),
    path('queries-list', views.get_queries_list, name='queries_list'),
    path('order/create', CreateOrder.as_view(), name='create_order'),
]
