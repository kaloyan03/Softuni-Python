# Generated by Django 4.0.1 on 2022-01-19 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todouser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todouser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
