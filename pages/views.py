import json

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.db import connection
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
    def count_services_cost(service_elements, outlet_id):
        transformed_services = []
        for service in service_elements:
            transformed_service = {
                'service_type_id': int(service['option']),
                'amount': int(service['count'])
            }
            if 'dropdownValues' in service:
                transformed_service['codes'] = service['dropdownValues']
            transformed_services.append(transformed_service)

        transformed_elements = {
            'services': transformed_services,
            'outlet_id': outlet_id
        }

        service_elements_json = json.dumps(transformed_elements)

        with connection.cursor() as cursor:
            cursor.execute("SELECT calculate_service_type_cost(%s::jsonb)", [service_elements_json])
            result = cursor.fetchone()[0]
            return result

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
        print(CreateOrder.count_services_cost(data['services'], 1))

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
