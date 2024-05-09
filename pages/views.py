from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from queries.urls import QUERIES_NUMBER


def index(request):
    return render(request, 'pages/index.html')


def get_queries_list(request):
    n = QUERIES_NUMBER
    context = {
        'queries_size': range(1, n + 1),
    }
    return render(request, 'pages/queries.html', context=context)


def create_order(request):
    return render(request, 'pages/create_order.html')


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Логин или пароль неверный."
        ),
        'inactive': _("Этот аккаунт заблокирован"),
    }


class LoginPageView(LoginView):
    template_name = 'pages/login.html'
    authentication_form = CustomAuthenticationForm

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class LogoutPageView(LogoutView):
    next_page = reverse_lazy('index')
