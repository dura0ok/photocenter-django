from django.db.models import Q
from django.shortcuts import render

from entities.models import OutletType
from .helpers import execute_query, build_response


def get_outlets():
    outlet_types = OutletType.objects.filter(
        Q(name='Филиал') | Q(name='Киоск') | Q(name='Фотомагазин')
    )
    return {'outlet_types': outlet_types}


def first_query(request):
    if request.method == 'POST':
        outlet_type_id = request.POST.get('outlet')
        query = "SELECT o.address, t.name FROM outlets o JOIN outlet_types t ON o.type_id = t.id WHERE o.type_id = %s"
        return build_response(*execute_query(query, (outlet_type_id,)))

    context = get_outlets()
    return render(request, 'pages/queries/1.html', context=context)


def second_query(request):
    if request.method == 'POST':
        outlet_type_id = request.POST.get('outlet')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')
        query = '''
        SELECT c.full_name,
               ot.address,
               o.accept_timestamp,
               ot_types.name AS accept_type
        FROM public.orders o
        JOIN public.outlets ot ON o.accept_outlet_id = ot.id
        JOIN public.outlet_types ot_types ON ot.type_id = ot_types.id
        JOIN clients c ON o.client_id = c.id
        WHERE ot.type_id = %s AND o.accept_timestamp BETWEEN %s AND %s
        '''
        return build_response(*execute_query(query, (outlet_type_id, start, end)))

    context = get_outlets()
    return render(request, 'pages/queries/2.html', context=context)
