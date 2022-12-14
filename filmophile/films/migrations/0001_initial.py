# Generated by Django 4.0.4 on 2022-08-17 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_member', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('information', models.TextField(blank=True, null=True)),
                ('role', models.ManyToManyField(to='films.role')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_film', models.CharField(blank=True, max_length=255, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='')),
                ('annotation', models.TextField(blank=True, null=True)),
                ('date_release', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('actors', models.ManyToManyField(blank=True, related_name='actors', to='films.member')),
                ('directors', models.ManyToManyField(blank=True, related_name='directors', to='films.member')),
                ('genre', models.ManyToManyField(blank=True, to='films.genre')),
                ('operators', models.ManyToManyField(blank=True, related_name='operators', to='films.member')),
                ('producers', models.ManyToManyField(blank=True, related_name='producers', to='films.member')),
                ('writers', models.ManyToManyField(blank=True, related_name='writers', to='films.member')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
