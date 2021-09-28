from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet

from api.models import Book, Author
from api.serializers import BookSerializer, AuthorSerializer
from api.filter import BooksListFilter


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BooksListFilter
    parser_classes = (JSONParser,)
    search_fields = ('title', 'authors')
    ordering_fields = ('created_at',)

    def get_queryset(self):
        if self.action == 'list':
            return Book.objects.prefetch_related('authors').distinct()
        else:
            return Book.objects.all().prefetch_related('authors')


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    parser_classes = (JSONParser,)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000


class LibraryView(BookViewSet):
    pagination_class = StandardResultsSetPagination
    search_fields = ('title', 'authors__author_name')
