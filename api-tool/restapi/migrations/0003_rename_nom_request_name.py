# Generated by Django 5.0.4 on 2024-04-17 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_request_nom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='nom',
            new_name='name',
        ),
    ]