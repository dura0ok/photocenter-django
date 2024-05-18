import json

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from entities.project_models import *
from queries.urls import QUERIES_NUMBER


def index(request):
    return render(request, 'pages/index.html')


def get_queries_list(request):
    n = QUERIES_NUMBER
    context = {
        'queries_size': range(1, n + 1),
    }
    return render(request, 'pages/queries.html', context=context)


@method_decorator(csrf_exempt, name='dispatch')
class CreateOrder(View):
    @staticmethod
    def get(request):
        outlet_id = request.user.outlet_id
        storage_items = StorageItem.objects.filter(storage__outlet_id=outlet_id).select_related('item')
        print_prices = PrintPrice.objects.all()

        service_types = ServiceType.objects.filter(
            servicetypeoutlet__outlet_type__outlet__id=outlet_id
        ).distinct()

        context = {
            'clients': Client.objects.all(),
            'services': service_types,
            'storage_items': storage_items,
            'print_prices': print_prices,
        }
        return render(request, 'pages/create_order.html', context=context)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        for service in data['services']:
            print(service)
            service_id = service['option']
            count = service['count']

        return JsonResponse({'success': True})


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
