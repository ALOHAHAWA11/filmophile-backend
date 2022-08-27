from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.role


class Member(models.Model):
    name_member = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    role = models.ManyToManyField(Role)

    def __str__(self):
        return self.name_member


class Genre(models.Model):
    genre_name = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.genre_name


class Film(models.Model):
    name_film = models.CharField(max_length=255, blank=True, null=True)
    original_name = models.CharField(max_length=255, blank=True, null=True)
    poster = models.ImageField(blank=True, null=True)
    annotation = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Genre, blank=True)
    date_release = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    actors = models.ManyToManyField(Member, blank=True, related_name='actors')
    directors = models.ManyToManyField(Member, blank=True, related_name='directors')
    operators = models.ManyToManyField(Member, blank=True, related_name='operators')
    writers = models.ManyToManyField(Member, blank=True, related_name='writers')
    producers = models.ManyToManyField(Member, blank=True, related_name='producers')

    def __str__(self):
        return self.name_film


class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
