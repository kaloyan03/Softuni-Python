# Generated by Django 4.0 on 2021-12-13 20:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=6)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
    ]
