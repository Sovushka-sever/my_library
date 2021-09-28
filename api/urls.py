from django.urls import path, include
from rest_framework import routers

from api.views import AuthorViewSet, BookViewSet, LibraryView

router_v1 = routers.DefaultRouter()
router_v1.register(r'authors', AuthorViewSet, basename='authors')
router_v1.register(r'books', BookViewSet, basename='books')
router_v1.register(r'library', LibraryView, basename='library')


urlpatterns = [
    path('api/v1/', include(router_v1.urls)),
]