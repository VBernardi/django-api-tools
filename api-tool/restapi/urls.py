from django.urls import path

from . import views

app_name = 'breach'


urlpatterns = [
    path('', views.index, name='index'),
]
