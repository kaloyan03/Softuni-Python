# Generated by Django 4.0.2 on 2022-02-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('expense_image', models.URLField()),
                ('description', models.TextField(null=True)),
                ('price', models.FloatField()),
            ],
        ),
    ]
