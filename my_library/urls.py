from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as docs_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'))
]

urlpatterns += docs_url
