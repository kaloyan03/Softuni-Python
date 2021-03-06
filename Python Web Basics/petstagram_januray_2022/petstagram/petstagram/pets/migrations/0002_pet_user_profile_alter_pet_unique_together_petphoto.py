# Generated by Django 4.0.2 on 2022-02-21 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('user_profile', 'name')},
        ),
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tagged_pets', models.ManyToManyField(to='pets.Pet')),
            ],
        ),
    ]
