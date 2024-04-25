from django import forms

from .models import Request

class RequestForm(forms.Form):
    HTTP_METHOD=(
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE'),
        ('HEAD', 'HEAD'),
        ('OPTIONS', 'OPTIONS'),
    )
    
    url = forms.URLField(label="")
    name = forms.CharField(label="")
    last_data = forms.JSONField(label="")
    http_method = forms.ChoiceField(label="", choices=HTTP_METHOD)

    class Meta:
        model = Request
        fields = ( "url", "name", "last_data", "http_method")
