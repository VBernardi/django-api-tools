# Generated by Django 5.0.4 on 2024-04-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='nom',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
