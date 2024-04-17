from django.urls import path

from .views import *

app_name = 'restapi'


urlpatterns = [
    path('', index, name="index"),
    path('<int:request_id>', index, name="index"),
    path('b/', basic_display_get, name='b'),
]
