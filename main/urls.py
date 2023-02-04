
from django.contrib import admin
from django.urls import path, include
from .drf_yasg import urlpatterns as url_swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('accounts.urls')),
]

urlpatterns += url_swagger