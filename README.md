# Api для my_library
API для электронной библиотеки

### Стек технологий:

- Ubuntu 20.04.1
- Python 3.7.6
- Django 3.2.7
- DRF 3.12.2

### Установка

Для начала вам нужно склонировать репозиторий в требуемую директорию
```
git clone https://github.com/Sovushka-sever/my_library.git
```
- Настроить виртуальное окружение и его активировать:
```
source venv/bin/activate
```
- Перейти в корневую папку проекта и установите все требуемые пакеты:
```
pip install -r requirements.txt
```
- Создайте миграции:
```
python3 manage.py makemigrations
```
- Выполнить миграции:
```
python3 manage.py migrate
```
- Запустите сервер: 
```
python3 manage.py runserver
```

## Дополнительные команды

- Для заполнения базы начальными данными есть 2 способа:
  - можно воспользоваться командой, которая создаст рандомные данные:

```
python3 manage.py random_fake
```
- 
  - или подгрузить данные из фикстур:
```
python3 manage.py loaddata fixtures.json
```
- Для создания суперюзера:
```
python3 manage.py createsuperuser
```
## Использование

- При запущеном сервере, на вкладке /api/v1 вы можете пройти по следующим эндпоинтам:
    - [authors](http://localhost:8080/api/v1/authors) - список авторов;
    - [books](http://localhost:8080/api/v1/books) - список книг с их авторами;
    - [library](http://localhost:8080/api/v1/library) - книги с их авторами по страницам;

Для того, чтобы удалить или редактировать запись нужно перейти к конкретной записи по ее id. 
- Пример:
    - [authors/39](http://localhost:8081/api/v1/authors/39/)

## Спецификация

Более подробный функционал представлен во [спецификации](http://127.0.0.1:8000/swagger/)
(доступно при запуске проекта)

Спецификация сгенерирована при помощи drf-yasg

## Авторы

* **Sovushka-sever** 

## Лицензия

Этот проект находится под лицензией Apache License 2.0. Подробности в файле  [LICENSE](https://github.com/Sovushka-sever/infra_sp2/blob/master/LICENSE)
