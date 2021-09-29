from rest_framework import filters
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet

from api.models import Book, Author
from api.serializers import BookSerializer, AuthorSerializer
from api.filter import BooksListFilter
from api.utils import StandardResultsSetPagination


class BookViewSet(ModelViewSet):
    """
    API для создания, редактирования книг и получения их списка.
    """
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
    """
    API для создания, редактирования авторов книг и получения их списка.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    parser_classes = (JSONParser,)


class LibraryView(BookViewSet):
    """
    API для постраничного просмотра книг с их авторами.
    """
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'authors__author_name')
