from django.db import models

from django.urls import reverse

class Request(models.Model):
    HTTP_METHOD=(
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE'),
        ('HEAD', 'HEAD'),
        ('OPTIONS', 'OPTIONS'),
    )
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=100, blank=True)
    last_data = models.JSONField(null=True, blank=True)
    http_method = models.CharField(max_length=7, choices=HTTP_METHOD, default='GET')


    def get_absolute_url(self):
        return reverse('restapi:index', args=[self.id])
    
    def __str__(self):
        return self.url