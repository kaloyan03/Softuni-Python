# Generated by Django 4.0 on 2021-12-12 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0008_todo_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
    ]
