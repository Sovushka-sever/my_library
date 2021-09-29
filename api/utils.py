from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    Постраничный пагинатор
    """
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000
