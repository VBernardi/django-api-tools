from django.contrib import admin
from .models import Request

@admin.register(Request)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['url', 'last_data', 'http_method']
    list_filter = ['http_method']