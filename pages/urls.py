from django.urls import path

from pages import views
from pages.views import LoginPageView, LogoutPageView

urlpatterns = [
    path('', views.index, name='index'),
    path('login', LoginPageView.as_view(), name='login'),
    path('logout', LogoutPageView.as_view(), name='logout'),
    path('queries-list', views.get_queries_list, name='queries_list'),
    path('order/create', views.create_order, name='create_order'),
]
