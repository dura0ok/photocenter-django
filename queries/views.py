from django.db.models import Q
from django.shortcuts import render

from entities.models import OutletType, Outlet
from .helpers import execute_query, build_success_response, build_error_response, validate_date_range


def get_outlets():
    outlet_types = OutletType.objects.filter(
        Q(name='Филиал') | Q(name='Киоск') | Q(name='Фотомагазин')
    )
    return {'outlet_types': outlet_types}


def get_list_total_points_photo_orders_intake(request):
    """1 запрос"""
    if request.method == 'POST':
        outlet_type_id = request.POST.get('outlet')
        query = '''
        SELECT o.address, t.name, o.num_workers 
        FROM outlets o 
        JOIN outlet_types t ON o.type_id = t.id 
        WHERE o.type_id = %s
        '''
        return build_success_response(*execute_query(query, (outlet_type_id,)))

    context = get_outlets()
    return render(request, 'pages/queries/1.html', context=context)


def get_orders_info_by_outlets(request):
    """2 запрос"""
    if request.method == 'POST':
        outlet_type_id = request.POST.get('outlet')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')
        valid, message = validate_date_range(start, end)
        if not valid:
            return build_error_response(message)
        query = '''
        SELECT c.full_name,
               ot.address,
               TO_CHAR(o.accept_timestamp, 'DD-MM-YYYY HH24:MI:SS') AS accept_timestamp,
               ot_types.name AS accept_type
        FROM public.orders o
        JOIN public.outlets ot ON o.accept_outlet_id = ot.id
        JOIN public.outlet_types ot_types ON ot.type_id = ot_types.id
        JOIN clients c ON o.client_id = c.id
        WHERE ot.type_id = %s AND o.accept_timestamp BETWEEN %s AND %s
        '''
        return build_success_response(*execute_query(query, (outlet_type_id, start, end)))

    context = get_outlets()
    return render(request, 'pages/queries/2.html', context=context)


def get_special_orders_type_by_outlets(request):
    """3 запрос"""
    if request.method == 'POST':
        outlet_type_id = request.POST.get('outlet')
        urgency = request.POST.get('urgency')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')

        valid, message = validate_date_range(start, end)
        if not valid:
            return build_error_response(message)

        query = '''
            SELECT 
                st.name,
                CASE WHEN o.is_urgent THEN 'Срочный' ELSE 'Не срочный' END AS is_urgent,
                TO_CHAR(o.accept_timestamp, 'DD-MM-YYYY HH24:MI:SS') AS accept_timestamp,
                c.full_name
            FROM 
                service_orders so
            JOIN 
                orders o ON so.order_id = o.id
            JOIN 
                service_types st ON so.service_type_id = st.id
            JOIN 
                public.clients c ON o.client_id = c.id
            JOIN 
                outlets ot ON o.accept_outlet_id = ot.id
            WHERE 
                ACCEPT_OUTLET_ID = %s 
                AND is_urgent = %s
                AND accept_timestamp BETWEEN %s AND %s;
        '''
        return build_success_response(*execute_query(query, (outlet_type_id, urgency, start, end)))

    outlets = Outlet.objects.select_related('type').filter(
        Q(type__name='Филиал') | Q(type__name='Киоск') | Q(type__name='Фотомагазин')
    )
    print(outlets)
    context = {'outlets': outlets}
    return render(request, 'pages/queries/3.html', context=context)
