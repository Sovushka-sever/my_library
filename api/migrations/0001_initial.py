# Generated by Django 3.2.7 on 2021-09-28 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('additional_information', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация об авторе')),
            ],
            options={
                'db_table': 'author',
                'ordering': ('-author_name',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название книги')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('authors', models.ManyToManyField(related_name='author_book', to='api.Author', verbose_name='Автор книги')),
            ],
            options={
                'db_table': 'book',
                'ordering': ('-created_at',),
            },
        ),
    ]