from django.db import connection
from django.http import JsonResponse


def execute_query(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        columns = [{"title": col[0], "field": col[0]} for col in cursor.description]
        data = cursor.fetchall()
        data_with_field_keys = [{col["field"]: row[i] for i, col in enumerate(columns)} for row in data]
        print(data_with_field_keys, cursor.query)
        return columns, data_with_field_keys


def build_success_response(columns, data_with_field_keys):
    return JsonResponse({'columns': columns, 'data': data_with_field_keys}, safe=False,
                        json_dumps_params={'ensure_ascii': False})


def build_error_response(message):
    return JsonResponse({'error': True, 'message': message}, safe=False, json_dumps_params={'ensure_ascii': False})
