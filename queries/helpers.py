import datetime

from django.db import connection
from django.http import JsonResponse

from queries.entities import *


def execute_query(query, params=None) -> QueryResult:
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        columns = [{"title": col[0], "field": col[0]} for col in cursor.description]
        data = cursor.fetchall()
        data_with_field_keys = [{col["field"]: row[i] for i, col in enumerate(columns)} for row in data]
        print(data_with_field_keys, cursor.query)
        return QueryResult(columns=columns, data=data_with_field_keys)


def build_success_response(responses: list[QueryResult]) -> JsonResponse:
    results = []
    for response in responses:
        results.append({'columns': response.columns, 'data': response.data})
    return JsonResponse({'results': results}, safe=False,
                        json_dumps_params={'ensure_ascii': False})


def build_error_response(message):
    return JsonResponse({'error': True, 'message': message}, safe=False, json_dumps_params={'ensure_ascii': False})


def validate_date_range(start, end):
    if not (start and end):
        return False, 'Укажите диапазон дат'
    try:
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d').date()
    except ValueError:
        return False, 'Неверный формат даты'
    if start_date > end_date:
        return False, 'Дата начала не может быть позже даты окончания'
    return True, (start_date, end_date)
