from django.db import models


class Author(models.Model):
    """
    Модель автора книг.
    """

    author_name = models.CharField(
        verbose_name='Имя автора',
        max_length=50,
        blank=False
    )
    additional_information = models.TextField(
        verbose_name='Дополнительная информация об авторе',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.author_name}'

    class Meta:
        ordering = ('-author_name',)
        db_table = 'author'


class Book(models.Model):
    """
    Модель книги.
    """
    title = models.CharField(
        verbose_name='Название книги',
        max_length=255,
        blank=False
    )
    authors = models.ManyToManyField(
        Author,
        verbose_name='Автор книги',
        related_name='author_book'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return f'Название книги: {self.title}'

    class Meta:
        ordering = ('-created_at',)
        db_table = 'book'

