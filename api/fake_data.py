import factory
from faker import Factory

from api.models import Author, Book

faker = Factory.create()


class AuthorFactory(factory.django.DjangoModelFactory):
    author_name = factory.LazyAttribute(lambda x: faker.first_name())
    additional_information = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = Author


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    description = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = Book

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return

        if not extracted:
            extracted = [AuthorFactory(), ]

        for author in extracted:
            self.authors.add(author)


