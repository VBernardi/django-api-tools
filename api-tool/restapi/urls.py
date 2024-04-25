from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'restapi'

urlpatterns = [
    path('', index, name="index"),
    path('<int:request_id>', index, name="index"),
    path('b/', basic_display_get, name='b'),
] + static(settings.STATIC_URL) \
  + static(settings.MEDIA_URL)
