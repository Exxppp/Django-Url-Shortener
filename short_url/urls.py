from django.urls import path

from short_url.views import links, create, info, delete_link

app_name = 'short_url'

urlpatterns = [
    path('', links, name='links'),
    path('create/', create, name='create'),
    path('delete/<str:short_url>', delete_link, name='delete_link'),
    path('info/', info, name='info'),
]
