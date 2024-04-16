from django.urls import path

from .views import index

app_name = 'breach'


urlpatterns = [
    path('', index, name='index'),
]
