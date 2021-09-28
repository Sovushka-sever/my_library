from rest_framework import serializers

from api.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения авторов книг.
    """

    class Meta:
        model = Author
        fields = (
            'id',
            'author_name',
            'additional_information',
        )


class BookSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения списка книг.
    """
    authors = AuthorSerializer(
        many=True,
    )

    def get_or_create_packages(self, authors):
        author_books = []
        for author in authors:
            author_instance, created = Author.objects.get_or_create(
                author_name=author.get('author_name'),
                additional_information=author.get('additional_information')
            )
            author_books.append(author_instance.pk)
        return author_books

    def create_or_update_packages(self, authors):
        author_books = []
        for author in authors:
            author_instance, created = Author.objects.update_or_create(
                author_name=author.get('author_name'),
                additional_information=author.get('additional_information')
            )
            author_books.append(author_instance.pk)
        return author_books

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)
        book.authors.set(self.get_or_create_packages(authors))
        book.save()
        return book

    def update(self, instance, validated_data):
        authors = validated_data.pop('authors', [])
        instance.authors.set(self.create_or_update_packages(authors))
        fields = ('title', 'description')
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:
                pass
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'authors',
            'description',
            'created_at',
        )
