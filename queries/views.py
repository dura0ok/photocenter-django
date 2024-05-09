from django.db.models import Q, QuerySet
from django.shortcuts import render
from django.views import View

from entities.models import OutletType, Outlet
from .helpers import *


def get_outlet_types():
    outlet_types = OutletType.objects.filter(
        Q(name='Филиал') | Q(name='Киоск') | Q(name='Фотомагазин')
    )
    return {'outlet_types': outlet_types}


def get_outlets():
    outlets = Outlet.objects.select_related('type').filter(
        Q(type__name='Филиал') | Q(type__name='Киоск') | Q(type__name='Фотомагазин')
    ).order_by('id')
    return {'outlets': outlets}


class Query1Handler(View):
    @staticmethod
    def get(request):
        context = get_outlet_types()
        return render(request, 'pages/queries/1.html', context=context)

    @staticmethod
    def post(request):
        outlet_type_id = request.POST.get('outlet')
        query = '''
                  SELECT o.address, o.num_workers 
                  FROM outlets o 
                  JOIN outlet_types t ON o.type_id = t.id 
                  WHERE o.type_id = %s
                  '''
        return build_success_response([execute_query(query, (outlet_type_id,), 'Адрес', 'Количество работников')])


class Query2Handler(View):
    @staticmethod
    def get(request):
        context = get_outlet_types()
        return render(request, 'pages/queries/2.html', context=context)

    @staticmethod
    def post(request):
        outlet_type_id = request.POST.get('outlet')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')
        try:
            start, end = validate_date_range(start, end)
        except ValueError as e:
            return build_error_response(str(e))

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

        return build_success_response(
            [
                execute_query(
                    query,
                    (outlet_type_id, start, end),
                    'ФИО', 'Адрес', 'Время приёма', 'Тип здания'
                )
            ]
        )


class Query3Handler(View):
    @staticmethod
    def get(request):
        context = get_outlets()
        return render(request, 'pages/queries/3.html', context=context)

    @staticmethod
    def post(request):
        outlet_type_id = request.POST.get('outlet')
        urgency = request.POST.get('urgency')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')

        try:
            start, end = validate_date_range(start, end)
        except ValueError as e:
            return build_error_response(str(e))

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

        return build_success_response([execute_query(query, (outlet_type_id, urgency, start, end))])


class Query4Handler(View):
    @staticmethod
    def get(request):
        context = get_outlets()
        return render(request, 'pages/queries/4.html', context=context)

    @staticmethod
    def post(request):
        outlet_id = request.POST.get('outlet')
        urgency = request.POST.get('urgency')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')

        try:
            start, end = validate_date_range(start, end)
        except ValueError as e:
            return build_error_response(str(e))
        query = '''
            SELECT ot.address, c.full_name, 
            TO_CHAR(o.accept_timestamp, 'DD-MM-YYYY HH24:MI:SS'), calculate_service_orders_price(o.id)
            FROM   orders o
            JOIN public.clients c on c.id = o.client_id
            JOIN outlets ot ON o.accept_outlet_id = ot.id
            WHERE  accept_outlet_id = %s
                   AND is_urgent = %s
                   AND accept_timestamp BETWEEN %s AND %s; ;
        '''
        resp = execute_query(query, (outlet_id, urgency, start, end), 'Адрес', 'Фио Клиента', 'Время',
                             'Стоимость услуг')
        resp.add_value_to_column_by_field(field_name="Стоимость услуг", key="topCalc", data="sum")
        return build_success_response([resp])


class Query5Handler(View):
    @staticmethod
    def get(request):
        context = get_outlets()
        context["all_outlets"] = True
        return render(request, 'pages/queries/5.html', context=context)

    @staticmethod
    def post(request):
        outlet_id = request.POST.get('outlet')
        urgency = request.POST.get('urgency')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')

        try:
            start, end = validate_date_range(start, end)
        except ValueError as e:
            return build_error_response(str(e))

        query = f'''
                    SELECT
                    ot.address,
                    c.full_name,
                    TO_CHAR(o.accept_timestamp, 'DD-MM-YYYY HH24:MI:SS'),
                    COALESCE(SUM(f.amount), 0)
                FROM
                    print_orders po
                JOIN 
                    orders o ON po.order_id = o.id
                JOIN
                    public.clients c ON c.id = o.client_id
                JOIN
                    outlets ot ON o.accept_outlet_id = ot.id
                LEFT JOIN
                    public.frames f ON po.id = f.print_order_id
                WHERE
                    o.is_urgent = %s
                    AND o.accept_timestamp BETWEEN %s AND %s 
                    {'AND o.accept_outlet_id = %s' if outlet_id else ''}
                    GROUP BY ot.address, c.full_name, o.accept_timestamp;
                '''

        args = [urgency, start, end]

        if outlet_id:
            args.append(outlet_id)

        resp = execute_query(
            query,
            args,
            'Адрес', 'ФИО', 'Дата', 'Количество'
        )

        resp.add_value_to_column_by_field(field_name="Количество", key="topCalc", data="sum")
        return build_success_response([
            resp
        ])

class Query6Handler(View):
        @staticmethod
        def get(request):
            context = get_outlets()
            context["all_outlets"] = True
            return render(request, 'pages/queries/6.html', context=context)

        @staticmethod
        def post(request):
            outlet_id = request.POST.get('outlet')
            urgency = request.POST.get('urgency')
            start = request.POST.get('start_date')
            end = request.POST.get('end_date')

            try:
                start, end = validate_date_range(start, end)
            except ValueError as e:
                return build_error_response(str(e))

            query = f'''
                            SELECT
                            ot.address,
                            c.full_name,
                            TO_CHAR(o.accept_timestamp, 'DD-MM-YYYY HH24:MI:SS'),
                            po.code
                        FROM
                            film_development_orders po
                        JOIN 
                            service_orders so on po.service_order_id = so.id
                        JOIN 
                            orders o ON so.order_id = o.id
                        JOIN 
                            outlets ot ON o.accept_outlet_id = ot.id
                        JOIN
                            clients c ON c.id = o.client_id
                    
                        WHERE
                            o.is_urgent = %s
                            AND o.accept_timestamp BETWEEN %s AND %s 
                            {'AND o.accept_outlet_id = %s' if outlet_id else ''}
                            GROUP BY ot.address, c.full_name, o.accept_timestamp, po.code;
                        '''

            args = [urgency, start, end]

            if outlet_id:
                args.append(outlet_id)

            resp = execute_query(
                query,
                args,
                'Адрес', 'ФИО', 'Дата', 'Код'
            )

            resp.add_value_to_column_by_field(field_name="Код", key="topCalc", data="count")
            return build_success_response([
                resp
            ])