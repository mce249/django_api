# Generated by Django 3.0.3 on 2020-02-06 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200206_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='url',
        ),
    ]