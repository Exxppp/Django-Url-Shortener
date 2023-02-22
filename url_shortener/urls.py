from django.contrib import admin
from django.urls import path, include

from short_url.views import index, short_url_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('users.urls', namespace='users')),
    path('links/', include('short_url.urls', namespace='short_url')),
    path('<str:short_url>', short_url_redirect, name='short_url_redirect'),
]
