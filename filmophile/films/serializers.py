from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.db.models import prefetch_related_objects

from .models import *


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ('role',)


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_name',)


class MemberPreviewSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ('pk', 'name_member')


class MemberSerializer(ModelSerializer):
    role = RoleSerializer(many=True)

    class Meta:
        model = Member
        fields = '__all__'


class FilmSerializer(ModelSerializer):
    actors = MemberPreviewSerializer(many=True)
    directors = MemberPreviewSerializer(many=True)
    operators = MemberPreviewSerializer(many=True)
    writers = MemberPreviewSerializer(many=True)
    producers = MemberPreviewSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Film
        fields = '__all__'


class FilmsSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = ('pk', 'name_film', 'poster', 'annotation', 'country',)


class CommentSerializer(ModelSerializer):
    film = serializers.HiddenField(default=Comment.film)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'
