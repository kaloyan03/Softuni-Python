# Generated by Django 4.0 on 2022-01-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='image_url',
        ),
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]