from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'per_page'
    page_query_param = 'page'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response(data)
