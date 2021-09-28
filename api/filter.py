from django_filters.rest_framework import (
    FilterSet,
    ModelMultipleChoiceFilter,
)

from api.models import Book, Author


class BooksListFilter(FilterSet):
    """
    Кастомный фильтр для BooksViewSet:
    выбор автора
    """
    author = ModelMultipleChoiceFilter(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ('author',)
