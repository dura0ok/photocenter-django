from django.db.models import Q
from django.shortcuts import render

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
        return build_success_response([execute_query(query, (outlet_type_id,))])

    context = get_outlet_types()
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
        return build_success_response([execute_query(query, (outlet_type_id, start, end))])

    context = get_outlet_types()
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
        return build_success_response([execute_query(query, (outlet_type_id, urgency, start, end))])

    context = get_outlets()
    return render(request, 'pages/queries/3.html', context=context)


def get_special_orders_revenue(request):
    """4ый запрос"""
    if request.method == 'POST':
        outlet_id = request.POST.get('outlet')
        urgency = request.POST.get('urgency')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')

        valid, message = validate_date_range(start, end)
        if not valid:
            return build_error_response(message)

        # First query
        query1 = '''
                WITH film_development_price AS (
                    SELECT
                        price
                    FROM
                        public.service_types
                    WHERE
                        public.service_types.name = 'Проявка плёнки'
                )
                SELECT
                    TO_CHAR(o.accept_timestamp, 'DD-MM-YYYY HH24:MI:SS') AS accept_timestamp,
                    c.full_name,
                    ROUND(SUM(
                    CASE
                        WHEN o2.accept_outlet_id = o.accept_outlet_id THEN 0
                        ELSE (SELECT price FROM film_development_price)
                    END) *
                    (100 - c.discount), 2) AS total_price
                FROM
                    public.film_development_orders fdo
                JOIN
                    public.orders o ON fdo.order_id = o.id
                JOIN
                    public.clients c ON c.id = o.client_id
                JOIN
                    films f ON fdo.code = f.code
                LEFT JOIN
                    sale_films sf ON f.id = sf.id
                LEFT JOIN sale_orders so ON sf.sale_order_id = so.id
                LEFT JOIN orders o2 ON so.order_id = o2.id
                WHERE
                    o.ACCEPT_OUTLET_ID = %s 
                    AND o.is_urgent = %s
                    AND o.accept_timestamp BETWEEN %s AND %s
                GROUP BY
                    fdo.order_id, c.discount, o.accept_timestamp, c.full_name;
            '''

        # Second query
        query2 = '''
                WITH DiscountedFrames AS (
                    SELECT
                        f.print_order_id,
                        pp.price * f.amount AS discounted_price,
                        COALESCE(
                            (SELECT MAX(pd.discount)
                             FROM public.print_discounts pd
                             WHERE pd.photo_amount <= (SELECT COUNT(*)
                                                       FROM public.frames
                                                       WHERE print_order_id = f.print_order_id)
                             GROUP BY pd.photo_amount), 0) / 100.0 AS discount
                    FROM
                        public.frames f
                    INNER JOIN
                        public.print_prices pp ON f.print_price_id = pp.id
                )

                SELECT
                    TO_CHAR(o.accept_timestamp, 'DD-MM-YYYY HH24:MI:SS') AS accept_timestamp,
                    c.full_name,
                    ROUND(SUM(df.discounted_price * (1 - df.discount)) *
                    (100 - c.discount), 2) AS total_amount
                FROM
                    public.print_orders po
                INNER JOIN
                    DiscountedFrames df ON po.id = df.print_order_id
                JOIN orders o on po.order_id = o.id
                JOIN clients c on c.id = o.client_id
                WHERE
                    ACCEPT_OUTLET_ID = %s 
                    AND is_urgent = %s
                    AND accept_timestamp BETWEEN %s AND %s
                GROUP BY
                    po.order_id, c.discount, o.accept_timestamp, c.full_name;
            '''

        # Execute queries and build response
        response1 = execute_query(query1, (outlet_id, urgency, start, end))
        response2 = execute_query(query2, (outlet_id, urgency, start, end))
        price_column = next(filter(lambda column: column["field"] == "total_price", response1.columns))
        price_column["topCalc"] = "sum"
        amount_column = next(filter(lambda column: column["field"] == "total_amount", response2.columns))
        amount_column["topCalc"] = "sum"

        print(response1, response2)
        return build_success_response([response1, response2])

    context = get_outlets()
    return render(request, 'pages/queries/4.html', context=context)


def get_prints_by_outlet(request):
    if request.method == 'POST':
        outlet_id = request.POST.get('outlet')
        start = request.POST.get('start_date')
        end = request.POST.get('end_date')

        query = '''
            SELECT
                CASE WHEN o.is_urgent THEN 'Срочный' ELSE 'Простой' END AS "Тип Заказа",
                COALESCE(SUM(f.amount), 0) AS "Количество отпечатанных фотографий"
            FROM
                public.orders o
            LEFT JOIN
                public.print_orders po ON o.id = po.order_id
            LEFT JOIN
                public.frames f ON po.id = f.print_order_id
                WHERE o.accept_outlet_id = %s AND o.accept_timestamp BETWEEN %s AND %s
            GROUP BY
                1;
        '''

        resp = execute_query(query, (outlet_id, start, end))
        return build_success_response([resp])
    """5ый запрос"""
    context = get_outlets()
    return render(request, 'pages/queries/5.html', context=context)
