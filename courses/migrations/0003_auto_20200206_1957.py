# Generated by Django 3.0.3 on 2020-02-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200206_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='url',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
